#!/usr/bin/env python

import Robot
import rospy

rospy.init_node('test')
robot = Robot.Robot('robot_0')

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.forward(1)
    rate.sleep()
