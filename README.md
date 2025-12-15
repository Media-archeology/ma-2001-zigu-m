# Plan de projet d'animation Atari 1040STF

Titre du projet: Animation en boucle "안녕" (points apparaissant et disparaissant)

#### Aperçu du projet

Objectif : Créer une animation en boucle où le texte "안녕" apparaît point par point puis disparaît progressivement dans un environnement 320×200 / 16 couleurs
Concept : Utiliser le mot coréen "안녕" pour symboliser le début et la fin(du semestre),les lettres se complètent et disparaissent point par point

####Scénario et mise en scène

Écran noir, les points apparaissent un par un pour former progressivement le mot "안녕"
Les points clignotent légèrement à leur apparition
->
Maintenir brièvement le texte complet pour transmettre le message
->
Les points disparaissent un par un, le texte se dissout progressivement
->
Répétition du cycle : apparition → maintien → disparition

####Plan technique

Tableau de points : Décomposer les lettres '안' et '녕' en points, créer des tableaux de structures Dot

Contrôle de l'animation : La variable displayCount contrôle le nombre de points affichés, points apparaissant/disparaissant à chaque frame

Timing frames/boucle : Boucle naturelle basée sur 50Hz

Environnement : Émulateur Hatari, TOS 1.04 ou EmuTOS, CPU 8MHz, affichage PAL 50Hz

Plan de travail DAY 1 — Installation et affichage minimal

Objectif: Configurer Hatari pour que le programme s’exécute et que l’écran affiche quelque chose
	1.	Installer et configurer Hatari
	2.	Charger l’image TOS
	3.	Créer le projet dans VS Code
	4.	Écrire un programme C minimal : écran noir → changement de couleur de fond
	5.	Appliquer le vsync
