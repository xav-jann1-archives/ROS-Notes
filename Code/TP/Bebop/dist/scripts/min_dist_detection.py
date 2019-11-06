#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32


class MinDist:
    """ Ros node that send the minimum distance from sensor
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('min_dist', anonymous=True)
        self.min_dist_pub = rospy.Publisher("/min_dist", Float32)
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)

    def scan_callback(self, data):
        """ Compute /scan data to publish only minimum distance
            * params:
                - data: LaserScan
        """
        ranges = np.array(data.ranges)
        ranges[np.isnan(ranges)] = data.range_max
        min_dist = np.min(ranges)

        rospy.loginfo(rospy.get_caller_id() + "min dist: %s", min_dist)
        self.min_dist_pub.publish(Float32(min_dist))


if __name__ == '__main__':
    md = MinDist()
    rospy.spin()
