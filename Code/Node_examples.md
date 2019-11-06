# Exemple de noeuds

## Turtle

Ouvrir une fenêtre avec la tortue:
`$ rosrun turtlesim turtlesim_node`

Contrôler la tortue avec les flèches du clavier (dans un autre terminal):
`$ rosrun turtlesim turtle_teleop_key`

Ajouter une tortue:
`$ rosrun call /spawn 2 2 0.2 ""`

Déplacer la tortue:
`$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'`
