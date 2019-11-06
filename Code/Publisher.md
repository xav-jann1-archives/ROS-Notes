# Publisher

## Syntaxe

**Code minimal pour utiliser `Publisher` dans un noeud:**

```python
pub = rospy.Publisher("<topic_name>", <msg_type>, queue_size = 10)
pub.publish(<data>)
```


## Exemple simple de Publisher

Envoie un message 10 fois par seconde:

```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
  pub = rospy.Publisher('chatter', String, queue_size = 10)
  rospy.init_node('talker', anonymous = True)
  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    hello_str = "hello world %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
```

### Détail du code:

```python
  pub = rospy.Publisher('chatter', String, queue_size = 10)
```
Crée un `topic` `chatter`, qui envoie des messages sous le type `String`
`queue_size`: permet de limiter le nombre de message dans la `queued message` si aucun `receiver` ne les reçoit assez vite


```python
  rospy.init_node('talker', anonymous=True)
```
Créé le noeud ROS (tant qu'il n'y a pas cette ligne, le programme ne peut pas communiquer avec le `ROS Master`)
`talker` est le nom du noeud (doit contenir des caratère "simple": pas de '/')
`anonymous`: ajoute un nombre aléatoire à la fin du nom pour s'assurer qu'il est unique


```python
  rospy.loginfo(hello_str)
```
Cette commande réalise 3 fonctions:
  - affiche le message sur l'écran
  - écrit le message dans les logs du noeud
  - écrit dans `rosout` (pour être utilisé avec `rqt_console`)


```python
if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
```
Le `try except` permet récupérer les exceptions produites par `rospy.sleep()` et `rospy.Rate.sleep()`
lorsque `CTRL+C` ou que le noeud doit s'éteindre.
Cette exception permet d'éviter d'exécuter accidentellement du code après `sleep()`.







