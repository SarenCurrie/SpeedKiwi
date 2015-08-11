#!/usr/bin/env python

import rospy
from robot import Robot
from animal import Animal
from different_robot import DifferentRobot
from move_action import MoveAction
from rotate_action import RotateAction
from navigate_action import NavigateAction
from math import pi

rospy.init_node('main')

robot = Robot('robot_0', 3, 0.05, 0, 0, pi/2)
robot1 = DifferentRobot('robot_1', 2, 2, 0, 0, pi/2)
animal = Animal('robot_2', 2, 2, 0, 0, pi/2)

robot.add_action(MoveAction(75))
robot.add_action(RotateAction("rotate_to_east"))
robot.add_action(MoveAction(3.5))
robot.add_action(RotateAction("rotate_to_south"))
robot.add_action(MoveAction(75))

# robot1.add_action(NavigateAction(50, 50))
# animal.add_action(NavigateAction(50, 50))

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()
    animal.execute()

    rate.sleep()
