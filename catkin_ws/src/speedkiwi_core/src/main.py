#!/usr/bin/env python

import rospy
from Robot import Robot
from DifferentRobot import DifferentRobot
from MoveAction import MoveAction
from RotateAction import RotateAction
from math import pi

rospy.init_node('main')
robot = Robot('robot_0', 0.5, 0.5, 0, 0, pi/4)
robot1 = DifferentRobot('robot_1', 2, 2, 0, 0, pi/2)

robot.add_action(RotateAction("rotate_to_south"))
robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(RotateAction("rotate_to_east"))
robot.add_action(MoveAction(5))
robot.add_action(RotateAction("rotate_to_west"))
robot.add_action(MoveAction(10))

robot1.forward()

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()

    rate.sleep()
