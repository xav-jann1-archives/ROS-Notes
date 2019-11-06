#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import Float64
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged as AltitudeType

# Publisher:
pub = 0

# Récupère et renvoie l'altitude du drone:
def altitude_handle(data):
    # Récupère l'altitude:
    altitude = data.altitude

    # Renvoie l'altitude:
    pub.publish(altitude)
    rospy.loginfo(rospy.get_caller_id() + " altitude: %s", altitude)


# Initialisation du noeud:   
def init():
    global pub

    # Init node:
    rospy.init_node('SubscriberAltitude', anonymous=True)

    # Subscriber:
    topic = "/bebop/states/ardrone3/PilotingState/AltitudeChanged"
    rospy.Subscriber(topic, AltitudeType, altitude_handle)
    
    # Publisher:
    pub = rospy.Publisher("/altitude", Float64, queue_size=10)


if __name__ == '__main__':
    # Initialisation du noeud:
    init()

    # Garde le noeud actif:
    rospy.spin()
