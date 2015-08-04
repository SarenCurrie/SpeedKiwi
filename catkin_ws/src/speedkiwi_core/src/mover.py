#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
from speedkiwi_core.msg import move

def mypub_node():
    publisher = rospy.Publisher('/robot_0/cmd_vel', Twist, queue_size=100)

    x = 0
    y = 0
    theta = 0

    rospy.init_node('mover')
    rate = rospy.Rate(10) # 10hz

    def move_handler(move):
        x = move.x
        y = move.y

    rospy.Subscriber('/robot_0/test', move, move_handler)

    while not rospy.is_shutdown():
        rate.sleep()

        msg = Twist() # replace existing similar assignments
        msg.linear.x = x
        msg.linear.y = y
        msg.angular.z = theta

        publisher.publish(msg)

if __name__ == '__main__':
    try:
        mypub_node()
    except rospy.ROSInterruptException:
        pass
