#!/usr/bin/env python
import rospy

from raptor_dbw_msgs.msg import *

def publish():
    rospy.init_node('test_pub',anonymous=True)
    pub = rospy.Publisher("vehicle/test_topic", test, queue_size = 10)
    test_msg = test()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        test_msg.test1 = 14
        test_msg.test2 = 28
        pub.publish(test_msg)
if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass

    