# Cours

ROS : Framework
Plusieurs version existe : à l'école version "Kinetic" (ou "Indigo")

## Créer un package

### Créer Workspace

Dans un dossier qui continet un dossier `src`, exécuter la commande :
`$ catkin_make`

(si erreur lors de la création, fini par `Invoking "cmake" failed` et avant `Make sure that you have installed "catkin_pkg", it is up to date and on the path PYTHONPATH`; exécuter: `$ export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages`)

Pour préparer l'environnement et d'autres ressources, afin d'utiliser le workspace :
`$ source devel/setup.bash`

Pour vérifier que `ROS_PACKAGE_PATH` contient le workspace créé :
`$ echo $ROS_PACKAGE_PATH`


### Créer package

Pour créer un nouveau package, en étant dans le dossier `src` du Workspace :
`$ carkin_create_pkg <package_name> [depend1] [depend2] [depend3]`


### Build workspace

Pour construire le workspace, en étant à la racine du workspace :
`$ catkin_make`

Pour ajouter le workspace à l'environnement ROS (peut être ajouter dans `.bashrc` pour automatiquement être exécuté) :
`$ . ~/catkin_ws/devel/setup.bash`


## Contruire un package

Pour construire les packages d'un workspace : (à exécuter à la racine du workspace)
`$ catkin_make`


## ROS Core

Démarrer **ROS Core** :
`$ roscore`

Un unique `roscore` peut fonctionner à la fois


## Nodes
`$ rosnode` :  récupérer des informations sur les noeuds

Lister les noeuds :
`$ rosnode list`

Pour avoir des informations sur un noeud (utiliser TAB pour autocompleter) :
`$ rosnode info <noeud>`

Pour tester la connexion avec un noeud :
`$ rosnode ping <node_name>`

Pour nettoyer `rosnode`, si des noeuds sont encore ouverts :
`$ rosnode cleanup`


## Rosrun
`$ rosrun` :  démarrer un noeud d'un package

Pour démarrer un noeud d'un package :
`$ rosrun [package_name] [node_name]`

Pour renommer un noeud :
`$ rosrun [package_name] [node_name] __name:=<new_name>`


## ROS Topic

Un `topic` permet à un noeud de **publier** (*publishing*) des données, pour que d'autres noeuds puissent s'y **inscrire** (*subscribes*)

Liste les commandes de `rostopic` :
`$ rostopic -h`

- `list` : liste tous les `topic` publiés et souscrits (*subcribed* and *published*)
`$ rostopic list`
`$ rostopic list -v` : informations détaillés sur les `topics`

- `echo` : affiche les données publiées par un `topic`
`$ rostopic echo [topic]`

- `pub` : publie des données comme un topic déjà existant
`$ rostopic pub [topic] [msg_type] [args]`

- `hz` : indique le rythme des données envoyées
`$ rostopic hz [topic]`

Pour avoir des informations complètes sur un topic :
`$ rostopic type [topic] | rosmsg show`


## ROS Messages

Les `Messages` correspondent aux données transmisent entre les noeuds. Un `message` a un `type` qui définit la forme (le contenu) du message.

Pour afficher le type de message utilisé par un `topic` publié (*published*) :
`$ rostopic type [topic]`

Pour avoir les détails d'un type de message :
`$ rosmsg show [type]`

## ROS srv

Pour afficher ce que contient le type d'un service :
`$ rossrv show [service type]`


## ROS Services

Un `service` permet à un noeud d'envoyer une **requête** à un autre noeud et attendre une **réponse**

Commandes de `rosservice` :
- `list` : affiche des informations sur les services en cours de fonctionnement

- `type` : affiche le type d'un service
`$ rosservice type [service]`
`$ rosservice type [service] | rossrv show` : information sur le type d'un service

- `call` : appelle un service avec des arguments (si nécessaire)
`$ rosservice call [service] [args]`

- `find` : chercher les services par type de service

- `uri` : affiche le service **ROSPC uri**

## ROS Param

Commandes de `rosparam` :
- `list` : liste les noms des paramètres

- `get` : récupère un paramètre
`$ rosparam get [param_name]`
`$ rosparam get /` : affiche tous les paramètres du `Parameter Service`

- `set` : défini un paramètre
`$ rosparam set [param_name] [value]`

- `load` : charge les paramètres depuis un fichier
`$ rosparam load [file_name] [namespace]`

- `dump` : écrit les paramètres dans un fichier
`$ rosparam dump [file_name] [namespace]`

- `delete` : supprime un paramètre


## ROS Launch

Lance un launch file :
`$ roslaunch [package] [filename.launch]`


## msg et srv

- `msg` : simple fichier texte qui décrit les champs d'un `message ROS` (utilisé pour générer le code source dans différents languages)
Stocké dans le dossier `msg` d'un package
Type utilisable dans un `message` :
  - `int8`, `int16`, `int32`, `int64`
  - `float32`, `float64`
  - `string`
  - `time`, `duration`
  - `other msg files`
  - `variable-length array[] and fixed-length array[C]`
  - `Header` : contient un `timestamp` et `coordinate frame information` qui sont souvent utilisé avec `ROS`

- `srv` : fichier qui décrit un `service`, composé de deux parties `request` et `response`
  Stocké dans le dossier `srv` d'un package
  Même type qu'un message, mais séparé en deux par `---` pour les parties `request` et `response`, exemple :
    ```go
    int64 A
    int64 B
    ---
    int64 sum
    ```
  `A`, `B` : `request` ; `Sum` : `response`


### Utilisation :

Etapes pour ajouter les fichiers `.msg` et/ou `.srv` dans la compilation du projet :  *cf. `Configure 'msg' and 'srv'.md`* 

Pour utiliser les messages et services dans un programme, il suffit d'ajouter :
```python
from <package_name>.msg import <msg_name>
from <package_name>.msg import <srv_name>
```

Et aussi avant d'exécuter le programme, ne pas oublier de sourcer : `$ source devel/setup.bash`


### Informations utiles :

- **Ne pas oublier de sourcer** pour chaque terminal ouvert : `$ source devel/setup.bash`
  Sinon les `messages` et `services` ne sont pas reconnus :
  Message d'erreur : `ERROR: Cannot load message class for [<pkg>/<msg_name>>]. Are your messages built?`

- **Ne pas utiliser le même nom** pour les `messages` et les `services` d'un même package, sinon erreur lors de `catkin_make install` :
  ```sh
  CMake Error: Attempt to add a custom rule to output ".../<workspace>/devel/include/<package>/<msg_name>.h.rule" which already has a custom rule.
  ```
