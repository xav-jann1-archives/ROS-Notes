#!/usr/bin/env python
import roslib
roslib.load_manifest('mini_projet')
import rospy
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged as AltitudeType

# Renvoie un TF avec l'altitude:
def handle_altitude(data, drone_name):
    altitude = data.altitude

    br = tf.TransformBroadcaster()
    br.sendTransform((0, 0, altitude),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     drone_name,
                     "world")


def listener():
    # Création du noeud:
    rospy.init_node('SubscriberAltitude', anonymous=True)

    # Subscriber:
    topic = "/bebop/states/ardrone3/PilotingState/AltitudeChanged"
    rospy.Subscriber('topic', AltitudeType, handle_altitude, "bebop")


if __name__ == '__main__':
    listener()
    rospy.spin()
