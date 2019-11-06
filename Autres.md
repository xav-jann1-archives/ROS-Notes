## Installation

Pour accéder aux commandes ROS: (à ajouter au `.bashrc`)
`source /opt/ros/<distro>/setup.bash`

## Overview of Filesystem Concepts
- Packages: unité
- Manifests:

### Filesystem
- `rospack` : permet de récupérer des informations sur les **packages**
- `roscd` : permet d'aller directement dans le dossier d'un **package** ou d'un **stack**
- `roscd log` : déplace dans le dossier où les logs sont sotckés
- `rosls` : `ls` directement dans le dossier d'un package

- `roscp`: copie un fichier d'un package dans le dossier en cours
`$ roscp [package_name] [file_to_copy_path] [copy_path]`
(exemple: `$ roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv`)


## Package

### Dependencies

Pour afficher les dépendances d'un package:
`$ rospack depends1 <package_name>`

Si erreur lors de l'utilisation de la commande `rospack`, vérifier l'exécutable Python utilisé:
`$ which python`
(peut se produire si le `.bashrc` contient un `export` qui modifie l'exécutable par défaut)

Toutes les dépendances sont contenues dans le fichier `package.xml`.


### Indirect dependencies

Pour afficher toutes les dépendances utilisées par l'ensemble des packages utilisé:
`$ rospavk depends <package_name>`


## ROSed

`rosed`: permet d'éditer directement les fichiers d'un package dans un éditeur de texte (par défaut: `VIM`)
Ne pas hésiter à utiliser la touche `TAB` (x2), pour afficher les fichiers d'un package
`$ rosed [package_name] [filename]`

Pour changer l'éditeur de texte par défaut:
`$ export EDITOR='nano -w'`
`$ export EDITOR='emacs -nw'`

(à ajouter dans `.bahsrc` pour être à automatiquement défini à chaque fois)