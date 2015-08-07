#!/usr/bin/env python

from Robot import Robot
from DifferentRobot import DifferentRobot
import rospy

rospy.init_node('test')
robot = Robot('robot_0', 0.5, 0.5, 0, 0, 0)
robot1 = DifferentRobot('robot_1', 2, 2, 0, 0, 0)

robot.forward()
robot1.forward()

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()

    rate.sleep()
