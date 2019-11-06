# Configure 'msg' and 'srv'

Etapes pour configurer le package pour correctement traiter les fichiers `.msg` et `.srv`.

Dans le dossier du package :

## Configuration pour `msg` ou `srv`

Pour que les fichiers soient utilisé dans le source code en C++, Python, ou autre,
il faut que les deux lignes suivantes se trouve dans le fichier `package.xml` du package:
```xml
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

Quelques modifications à réaliser dans le fichier `CMakeLists.txt`:
Pour générer des messages:
```php
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation # ligne à ajouter
)
```

Pour les `message runtime dependency` s'exporte bien:
```php
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...
)
```

Décommenter aussi les lignes suivantes, et remplacer `Message*.msg` par le fichiers `.msg` créés:
(Cela permet d'être certain que `CMake` sait comment configurer le projet avec les fichiers `.msg`)
```php
add_message_files(
  FILES
  Message1.msg
  Message2.msg
)
```

Enfin, il faut s'assurer que la fonction `generate_messages()` est bien appelé, en décommentant les lignes:
```php
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

## A ajouter pour `srv`

Dans `CMakeLists.txt`

Décommenter les lignes suivantes, et remplacer `Service*.srv` par les fichiers `.srv` créés:
```php
add_service_files(
  FILES
  Service1.srv
  Service2.srv
)
```


## Finalisation

Enfin, il est nécesaire de recompiler les `packages`:
En étant à l'origine du workspace:
`$ catkin_make install`

Si une erreur se produit, supprimer les dossiers `build`, `devel` et `install`, et réexécuter la commande:
`$ rm -rf build devel install `
`$ catkin_make install`

Cette étape permet de générer les `C++ messages header` des `messages` et `services` dans le dossier `devel/include/<package>/`
et les `Python script` dans `devel/lib/python2.7/dist-packages/<package>/(msg|srv)/`
 



