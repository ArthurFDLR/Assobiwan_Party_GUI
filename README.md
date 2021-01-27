# Assobiwan's drink sales manager

The main window is projected behind the bar while bartenders use the control window to register sales. Prices vary between 0.80€ and 1.20€ by 0.05€ steps. A team gains a point when one of its members buys a drink and loses one when the other team gets a drink. The 5ct fluctuation affects the prices when a team reaches 5 points.
![Main window](MainWindow.PNG)

Use [pipenv](https://pypi.org/project/pipenv/) with Pipfile provided to create an adequate Python interpreter.

## Invasion mode

To activate Invasion Mode, click "mode invasion" on the control panel, click once again to deactivate. During Invasion, prices are set to 1.00€ (regardless of each team's scores). However, points are still evolving. Thus prices are different at the end of Invasion mode from what they used to be at the beginning.

## Control pannel

When a bartender sells a drink, he needs to click "+1 pour les Siths/Jedis" according to the buyer's team (blue or red wristband). Large orders can be displayed, select the team, the number of drinks, the person's name, click "Go".
The log window registers all individual sales and the total sales number on "Totale des ventes" click.
The button "Reinitialisation de la partie" erases all data to restart a game.

![Control window](ControlWindow.PNG)
