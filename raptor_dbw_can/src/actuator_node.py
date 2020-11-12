#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
import random
import time
import math
from raptor_dbw_msgs.msg import *


if __name__ == '__main__':
    rospy.init_node('heartbeat')
    pub_heartbeat_to_raptor_new = rospy.Publisher('/vehicle/spacedrive', SpaceDrive, queue_size=1)

    rate = rospy.Rate(5)
    counter = 0
    theta = 0
    up = 1; down = 0
    while not rospy.is_shutdown():

        if theta >= 180:
            theta = 0
        actuator_msg = SpaceDrive()
        actuator_msg.counter = counter
        actuator_msg.brake_demand = 32000*math.sin(theta*math.pi/180)
        actuator_msg.gear_demand = 1
        actuator_msg.accelerator_demand = 100
        actuator_msg.steering_demand = 32000*math.sin(theta*math.pi/180)
        actuator_msg.trigger = 2
        actuator_msg.supervisor_input = 2#2 - Shutdown sequence; 0 - Startup sequence; 1 - Controlling sequence
        pub_heartbeat_to_raptor_new.publish(actuator_msg)
        counter += 1
        if counter == 255:
            counter = 0
        theta = theta + 1

        
        # previous_heartbeat = autonomy_beat_new
        rate.sleep()
    print('\nHeartbeat Broken')
