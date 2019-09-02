# Assobiwan's drink sales manager


Application used during ENSMA parties to record sales and adapt price over each teams consumption.

The main window is projected behind the bar, the control window is used by bartenders to register sales.

![Main window](img\MainWindow.PNG)
![Control window](img\ControlWindow.PNG)

## Principe de base

Permet d'afficher en temps reelle les prix des verres de cocktails de deux equipes, Jedi et Sith.
Les prix varient de 0.80€ à 1.20€ par 5ct. Le changement de prix repose sur un systeme de +1/-1.
Une equipe gagne 1 point quand elle achete un verre et en perd 1 quand l'adversaire en achete un.
Une baisse de 5ct est accordé lorsque l'equipe atteint 5 points.
(En partant de 0, si les Siths achetent 4 verres, les Jedi doivent en acheter 9 pour baisser le prix)


## Invasion

Pour activer l'invasion, cliquer sur le bouton "mode invasion" du panneau de commande, de même pour la désactiver.
Dans ce mode, le prix est fixé à 1€ pour les deux equipes. Cependant, les prix continuent d'evoluer de maniere cachée.
En fin d'invasion, les prix de ventes sont à nouveaux ceux ayant évolué du début de l'invasion.

## Panneau de commande

Lorsque vous vendez un verre, cliquez sur "+1 pour les Siths" ou "+1 pour les Jedis".
(Il est aussi possible de cliquer sur le logo de l'équipe correspondante dans la fenetre d'affichage)
Vous pouvez afficher une grosse commande d'un ensmatique en séléctionnant son équipe, 
le nombre de verres achetés et son nom puis en appuyant sur "Go" sous les boutons de ventes.
(Possibilité d'en faire une concours des plus grosses commandes ...)
Un clique sur "Total des ventes" affiche le total des ventes de la soirée 