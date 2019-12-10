## rqt

`$ rqt`: Fenêtre principale qui contient un menu déroulant avec tous les outils proposés

- `rqt_graph`: affiche un graph des communications entre noeuds:
`$ rosrun rqt_graph rqt_graph`

En plaçant la souris sur les éléments, leur couleur change:
- bleu, vert: nodes
- rouge: topics


- `rqt_plot`: pour afficher des graphs sur l'évolution des données au cours du temps:
`$ rosrun rqt_plot rqt_plot`

Utiliser la touche `-`, pour ...

- `rqt_console`: `ROS's logging framework` pour afficher les sorties des noeuds
`$ rosrun rqt_console rqt_console`

- `rqt_logger_level`: permet de changer le `verbosity level` (`Debug`, `Warn`, `Info`, `Erro`, `Fatal`) de noeuds pendant leur fonctionnement
`$ rosrun rqt_logger_level rqt_logger_level`
