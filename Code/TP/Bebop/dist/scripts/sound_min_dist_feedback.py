#!/usr/bin/env python
import rospy
from kobuki_msgs.msg import Sound, Led
from std_msgs.msg import Float32, UInt8


class SoundDetect:
    """ Ros node that generate sound based on the minimum distance detected
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('sound_min_dist', anonymous=True)

        # Sound:
        self.sound_pub = rospy.Publisher("/mobile_base/commands/sound", Sound)
        rospy.Subscriber('/min_dist', Float32, self.min_dist_callback)
        self.send_sound = False

        # LED:
        self.led_pub = rospy.Publisher("/mobile_base/commands/led1", Led)
        self.led_state = True

    def loop(self):
        """ Make continuously sound after the first detection
        """
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.send_sound:
                self.sound_pub.publish(Sound(3))
                self.toogle_led()
            self.rate.sleep()

    def toogle_led(self):
        """ Toggle the LED on the robot
        """
        self.led_state = not self.led_state
        rospy.loginfo(rospy.get_caller_id() + "toggle led: %s ", self.led_state)
        i = 1 if self.led_state else 0
        self.led_pub.publish(Led(i))

    def min_dist_callback(self, data):
        """ Change the rate of the sound
            * params:
                - data: Float32
        """
        min_dist = data.data
        f = 2 / min_dist
        self.rate = rospy.Rate(f)
        rospy.loginfo(rospy.get_caller_id() + "new rate: %s ", data.data)
        self.send_sound = True


if __name__ == '__main__':
    s = SoundDetect()
    s.loop()
