#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


class SafeInput:
    """ Ros node that transmit data from input command
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('safe_vel_cmd_crt', anonymous=True)
        self.cmd_vel_safe_pub = rospy.Publisher("/cmd_vel_safe_output", Twist)
        rospy.Subscriber('/cmd_vel_safe_input', Twist , self.cmd_callback)

    def cmd_callback(self, data):
        """ Send back data from input topic to output
            * params:
                - data: Twist
        """
        rospy.loginfo(rospy.get_caller_id() + " %s", data)
        self.cmd_vel_safe_pub.publish(data)


if __name__ == '__main__':
    si = SafeInput()
    rospy.spin()
