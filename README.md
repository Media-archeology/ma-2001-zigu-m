# Plan de projet d'animation Atari 1040STF

### Titre du projet: Animation en boucle "안녕" (points apparaissant et disparaissant)

### Aperçu du projet

Objectif : Créer une animation en boucle où le texte "안녕" apparaît point par point puis disparaît progressivement dans un environnement 320×200 / 16 couleurs
<br>Concept : Utiliser le mot coréen "안녕" pour symboliser le début et la fin(du semestre),les lettres se complètent et disparaissent point par point

### Scénario et mise en scène

Écran noir, les points apparaissent un par un pour former progressivement le mot "안녕"
<br>Les points clignotent légèrement à leur apparition
<br>->
Maintenir brièvement le texte complet pour transmettre le message
<br>->
Les points disparaissent un par un, le texte se dissout progressivement
<br>->
Répétition du cycle : apparition → maintien → disparition

### Plan technique

Tableau de points : Décomposer les lettres '안' et '녕' en points, créer des tableaux de structures Dot

Contrôle de l'animation : La variable displayCount contrôle le nombre de points affichés, points apparaissant/disparaissant à chaque frame

Timing frames/boucle : Boucle naturelle basée sur 50Hz

Environnement : Émulateur Hatari, TOS 1.04 ou EmuTOS, CPU 8MHz, affichage PAL 50Hz

### Plan de travail 

Objectif: Configurer Hatari pour que le programme s’exécute et que l’écran affiche quelque chose

#### DAY 1 — Installation et affichage minimal

	1.	Installer et configurer Hatari
	2.	Charger l’image TOS
	3.	Créer le projet dans VS Code
	4.	Écrire un programme C minimal : écran noir → changement de couleur de fond
	5.	Appliquer le vsync

### Processus

Au départ, le projet devait être réalisé à l’aide du compilateur le plus traditionnellement utilisé pour le développement sur Atari ST :
VBCC (Volker Barthelmann C Compiler).

VBCC prend officiellement en charge la cible Atari ST / TOS (m68k-atari), permet de générer des fichiers .PRG exécutables sur du matériel Atari réel, et constitue un outil fréquemment utilisé avec l’émulateur Hatari.

#### Problèmes rencontrés
•	Incompatibilité de plateforme
	La majorité des distributions officielles de VBCC sont destinées à Atari MiNT ou à des systèmes Linux x86 anciens, ce qui les rend directement incompatibles avec l’environnement Apple Silicon (M1/M2, ARM).
•	Séparation stricte entre le compilateur et les cibles
	L’architecture de VBCC impose une installation distincte du compilateur, des définitions de cibles et des bibliothèques, ce qui complique fortement la configuration et l’utilisation dans un contexte de projet pédagogique.

#### Conclusion
<br>→ Transition vers une compilation croisée basée sur GCC
