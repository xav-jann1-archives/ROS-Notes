#!/usr/bin/env python
import rospy
from kobuki_msgs.msg import BumperEvent, Sound


class Collision:
    """ Ros node that detect collision
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('listener', anonymous=True)
        self.sound_pub = rospy.Publisher("/mobile_base/commands/sound", Sound, queue_size=10)
        rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.bumper_callback)

    def bumper_callback(self, data):
        """ Emit a sound when a collision occured
            * params:
                - data: BumperEvent
        """
        rospy.loginfo(rospy.get_caller_id() + "I heard %s %s", data.bumper, data.state)
        if data.state == 1 :
            s = Sound(3)
            self.sound_pub.publish(s)


if __name__ == '__main__':
    c = Collision()
    rospy.spin()