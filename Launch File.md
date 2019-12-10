# Launch File

Fichier à mettre dans un dossier `launch` d'un package.

Fichier au format `XML`:
```XML
<launch>
  <!-- Remap du launch file pour relier les topics
       d'un noeuds avec les topics du roscore -->
  <remap from="<topic>" to="<topic>"/>
  <remap from="<topic>" to="<topic>"/>
  
  <!-- Importer un autre launch file -->
  <include file="$(find <pkg_name>)/launch/<launch_name>.launch" />

  <!-- Création d'un groupe (évite des conflits de variables) -->
  <group ns="<groupe_name>">
    <node pkg="<package>" name="<name>" type="<type>"/>
  </group>

  <!-- Création d'un noeud -->
  <node pkg="<package" name="<name>" type="<type>">
    <!-- Relie les noeuds pour exécuter les mêmes actions-->
    <remap from="input" to=""/>
    <remap from="output" to=""/>
  </node>


</launch>
```