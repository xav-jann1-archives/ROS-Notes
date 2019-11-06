""" Class minimale """

#!/usr/bin/env python
import rospy

class ClassName:
    """ Ros node that ...
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('listener', anonymous=True)


if __name__ == '__main__':
    c = ClassName()
    rospy.spin()



""" Class complète """

#!/usr/bin/env python
import rospy

class ClassName:
    """ Ros node that ...
    """

    def __init__(self):
        self.config_ros()

    def config_ros(self):
        rospy.init_node('listener', anonymous=True)

        # Publisher:
        self.pub = rospy.Publisher("<topic>", <Type>, queue_size=10)
        
        # Subscriber:
        rospy.Subscriber('<topic>', <Type>, self.msg_callback)

        # Service:
        self.s = rospy.Service('<service_name>', <service_type>, self.srv_callback)


    def msg_callback(self, data):
        """ Message Callback
        """
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.<value>)

    def srv_callback(self, data):
        """ Service Callback
        """
        a, b = data.a, data.b
        res = ...
        return <service_type>Response(res, ...)

    
    def request_service(self, a, b):
        """ Service Client
        """
        try:
            service = rospy.ServiceProxy('<service_name>', <service_type>)
            res = service(...args)
            return res
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e


if __name__ == '__main__':
    c = ClassName()

    rospy.wait_for_service('<service_name>')
    c.requestService(a, b)
    rospy.spin()
