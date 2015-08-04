#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 

def mypub_node():
    mypub_object = rospy.Publisher('cmd_vel', Twist, queue_size=100) #my_handle.advertise<Twist>("cmd_vel", 100);

    rospy.init_node('mypub_node')
    rate = rospy.Rate(10) # 10hz

    counter = 0

    while not rospy.is_shutdown():
        rate.sleep()

        mypub_msg = Twist() # replace existing similar assignments
        mypub_msg.linear.x = 1
        mypub_msg.linear.z = 0.1
        mypub_msg.angular.z = 0.5

        mypub_object.publish(mypub_msg)

if __name__ == '__main__':
    try:
        mypub_node()
    except rospy.ROSInterruptException:
        pass