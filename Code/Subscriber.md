# Subscriber

## Syntaxe

**Code minimal pour utiliser `Subscriber` dans un noeud:**

```python
rospy.Subscriber("<topic_name>", <msg_type>, <callback>)
```


## Exemple simple

```python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
  rospy.init_node('listener', anonymous=True)

  rospy.Subscriber("chatter", String, callback)

  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()

if __name__ == '__main__':
  listener()
```