# URDF

`$ catkin_create_pkg <pkg_name> roscpp tf geometry_msgs urdf rviz xacro`

## Fichier URDF:
`$ sudo apt install liburdfdom-tools`

- Vérifier le contenu d'un fichier URDF:
`$ check_urdf <name>.urdf`

- afficher la structure contenu dans le fichier:
`$ urdf_to_graphiz <name>.urdf`
(génère deux fichiers: `.gv` et `.pdf`)
(Convertir `.gv` en `.png` : `dot -Tpng InputFile.gv -o OutputFile.png`)


## Fichier xacro:

Premières lignes d'un fichier `.xacro` pour indiquer que le format `xacro` est utilisé:
```xml
<?xml version="1.0"?>
<robot name="<robot_name>" xmlns:xacro="http://ros.org/wiki/xacro">
```

**Conversion d'un fichier `.xacro` en `.urdf`**:
`$ rosrun xacro xacro <name>.xacro --inorder > <name>.urdf`

Conversion d'un fichier `xacro` dans un `launch file`:
```xml
<param name="robot_description" command="$(find xacro)/xacro --inorder $(find <pkg_name>)/urdf/<name>.xacro"/>
```

