# Transform Frame


## TF Broadcaster

```python
import tf

br = tf.TransformBroadcaster()
br.sendTransform(   (x, y, z),
                    tf.transformations.quaternion_from_euler(0, 0, theta),
                    rospy.Time.now(),
                    <tf_child>, <tf_parent>)
```

## TF Listener

```python
import tf
...

listener = tf.TransformListener(0)

try:
    (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    continue
```

## Debug

Récupérer des informations 
`$ rosrun tf tf_echo <tf1> <tf2>`

Afficher une représentation graphique des TFs:
`$ rosrun tf view_frames` : crée la représentation
`$ evince frames.pdf` : affiche la représentation


Afficher des statistiques entre deux TFs:
`$ rosrun tf tf_monitor <tf1> <tf2`

