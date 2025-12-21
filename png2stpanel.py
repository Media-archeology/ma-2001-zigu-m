#!/usr/bin/env python3
"""
Convert PNG into Atari ST low-res planar 4bpp data
using a FIXED palette matching the game palette.
"""

import sys
import os
from PIL import Image

# =========================
# FIXED GAME PALETTE (RGB)
# =========================
GAME_PALETTE_RGB = [
    (0, 0, 0),          # 0 black
    (52, 46, 46),       # 1 dark gray/brown
    (7, 144, 0),        # 2 green
    (182, 0, 0),        # 3 red
    (255, 252, 213),    # 4 cream
    (254, 169, 188),    # 5 pink
    (255, 255, 255),    # 6 white
    (124, 11, 15),      # 7 dark red
]

def rgb_to_st(r, g, b):
    r3 = (r >> 5) & 0x7
    g3 = (g >> 5) & 0x7
    b3 = (b >> 5) & 0x7
    return (r3 << 8) | (g3 << 4) | b3

def sanitize_name(name: str) -> str:
    out = []
    for c in name:
        out.append(c.lower() if c.isalnum() else '_')
    s = ''.join(out)
    if s and s[0].isdigit():
        s = '_' + s
    return s

def dist2(c, t):
    return (c[0]-t[0])**2 + (c[1]-t[1])**2 + (c[2]-t[2])**2

def nearest_palette_index(rgb):
    best = 0
    best_d = 1e18
    for i, p in enumerate(GAME_PALETTE_RGB):
        d = dist2(rgb, p)
        if d < best_d:
            best_d = d
            best = i
    return best

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 png2stpanel.py input.png output.h")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    base = os.path.splitext(os.path.basename(in_path))[0]
    var = sanitize_name(base)

    img = Image.open(in_path).convert("RGBA")
    w, h = img.size
    if w % 16 != 0:
        print(f"ERROR: width must be multiple of 16. got {w}")
        sys.exit(1)

    # Alpha -> black
    bg = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    img = Image.alpha_composite(bg, img).convert("RGB")

    pixels = list(img.getdata())

    # Map pixels to fixed palette indices
    indexed = [nearest_palette_index(p) for p in pixels]

    # Build planar data
    data = bytearray()
    blocks_per_line = w // 16

    for y in range(h):
        row = y * w
        for b in range(blocks_per_line):
            p0 = p1 = p2 = p3 = 0
            for i in range(16):
                idx = indexed[row + b*16 + i]
                bit = 15 - i
                if idx & 1: p0 |= (1 << bit)
                if idx & 2: p1 |= (1 << bit)
                if idx & 4: p2 |= (1 << bit)
                if idx & 8: p3 |= (1 << bit)
            data += bytes([
                (p0 >> 8) & 0xFF, p0 & 0xFF,
                (p1 >> 8) & 0xFF, p1 & 0xFF,
                (p2 >> 8) & 0xFF, p2 & 0xFF,
                (p3 >> 8) & 0xFF, p3 & 0xFF
            ])

    # Write header
    with open(out_path, "w") as f:
        f.write(f"/* Auto-generated from {os.path.basename(in_path)} */\n")
        f.write(f"#ifndef {var.upper()}_PANEL_H\n")
        f.write(f"#define {var.upper()}_PANEL_H\n\n")
        f.write(f"#define {var.upper()}_W {w}\n")
        f.write(f"#define {var.upper()}_H {h}\n\n")

        f.write(f"static const unsigned short {var}_palette[16] = {{\n")
        for i in range(16):
            if i < len(GAME_PALETTE_RGB):
                r, g, b = GAME_PALETTE_RGB[i]
                f.write(f"    0x{rgb_to_st(r,g,b):04X},\n")
            else:
                f.write("    0x0000,\n")
        f.write("};\n\n")

        f.write(f"static const unsigned char {var}_data[{len(data)}] = {{\n")
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            f.write("    " + ", ".join(f"0x{b:02X}" for b in chunk))
            if i + 16 < len(data):
                f.write(",")
            f.write("\n")
        f.write("};\n\n")
        f.write("#endif\n")

    print("OK:", out_path)
    print("Palette: FIXED (game palette)")
    print("Panel:", w, "x", h)
    print("Data bytes:", len(data))

if __name__ == "__main__":
    main()