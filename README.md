# Plan de projet d'animation Atari 1040STF

### Titre du projet: Strawberry Escape

### Aperçu du projet

- Jeu d’action de style arcade où le joueur contrôle un personnage pour éviter les blocs de fraises tombant du haut de l’écran
- **Plateforme :** Atari ST
- **Objectif final :** Exécutable sur un véritable Atari 1040STF
- **Gameplay principal :** Éviter les blocs (fraises) en se déplaçant à gauche et à droite

### Scénario et mise en scène

Le joueur doit déplacer le personnage à gauche et à droite en bas de l’écran pour éviter les fraises tombant du haut. Le déroulement du jeu est le suivant :

1. ### Instructions de jeu

2. ### Écran de démarrage

- Affichage du titre principal “Strawberry Escape !” et du bouton START
- Le joueur appuie sur la barre d’espace ou sur Entrée pour commencer le jeu

3. ### Gameplay

- Le joueur déplace le personnage avec les flèches gauche et droite
- Des blocs de fraises tombent à des positions aléatoires à intervalles réguliers
- Collision avec un bloc = fin du jeu
- Éviter les blocs augmente le score

4. ### Écran de fin de jeu

- Affichage du texte “GAME OVER” et du score
- Bouton RESTART avec image du personnage

5. ### Crédits

### Éléments techniques

#### Graphismes

- Résolution 320×200 utilisant la palette 16 couleurs de l’Atari ST
- Les sprites du personnage et des blocs sont stockés en mode plan (4 bits)
- Gestion de la transparence et double buffering basé sur un tampon pour minimiser le clignotement

#### Rendu du texte

- Utilisation de caractères 8×8 pixels basés sur la police système
- Fonctionnalités de centrage et double taille (drawText2x, drawTextCentered)
- Support des majuscules, chiffres et certains caractères spéciaux

#### Logique du jeu

- Basée sur une machine à états : START → PLAYING → GAMEOVER
- Vérification des collisions avec la méthode AABB
- Apparition aléatoire des blocs et système de score

#### Gestion des entrées

- Gestion du clavier Atari ST (Cconis, Cnecin)
- Déplacement gauche/droite, démarrage/restart, sortie (Esc)

### Plan

1. #### Conception du jeu

- Choisir l’idée d’un jeu d’arcade simple basé sur l’évitement
- Déterminer la disposition de l’écran, le personnage, la taille et la vitesse des blocs

2. #### Création graphique

- Dessiner le personnage et les blocs pixel par pixel
- Convertir les fichiers png en données plan 4 bits

3. #### Implémentation du texte et des polices

- Écrire des fonctions pour dessiner les caractères en utilisant la police système
- Implémenter les fonctions de centrage et d’agrandissement

4. #### Implémentation de la logique du jeu

- Concevoir la structure de la machine à états
- Implémenter la vérification des collisions et l’apparition des blocs
- Mettre en place le système de score et les conditions de fin de jeu

5. #### Tests et débogage

- Vérifier l’affichage des sprites et corriger les erreurs de buffering
- Ajuster la réactivité des entrées clavier
- Vérifier les éléments UI tels que le centrage et l’agrandissement

### Processus

Au départ, le projet devait être réalisé à l’aide du compilateur le plus traditionnellement utilisé pour le développement sur Atari ST :
VBCC (Volker Barthelmann C Compiler).

VBCC prend officiellement en charge la cible Atari ST / TOS (m68k-atari), permet de générer des fichiers .PRG exécutables sur du matériel Atari réel, et constitue un outil fréquemment utilisé avec l’émulateur Hatari.

#### Problèmes rencontrés
•	Incompatibilité de plateforme
	<br>La majorité des distributions officielles de VBCC sont destinées à Atari MiNT ou à des systèmes Linux x86 anciens, ce qui les rend directement incompatibles avec l’environnement Apple Silicon (M1/M2, ARM).
<br>•	Séparation stricte entre le compilateur et les cibles
	<br>L’architecture de VBCC impose une installation distincte du compilateur, des définitions de cibles et des bibliothèques, ce qui complique fortement la configuration et l’utilisation dans un contexte de projet pédagogique.

#### Conclusion
<br>→ Transition vers une compilation croisée basée sur GCC

#### Les sprites
<img src="../ma-2001-zigu-m/img/player.png" title="" alt="player.png" width="32">
<img src="../ma-2001-zigu-m/img/gameover.png" title="" alt="gameover.png" width="32">
<img src="../ma-2001-zigu-m/img/block.png" title="" alt="block.png" width="16">
