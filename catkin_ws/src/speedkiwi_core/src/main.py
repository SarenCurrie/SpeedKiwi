#!/usr/bin/env python

import rospy
from robot import Robot
from animal import Animal
from person import Person
from different_robot import DifferentRobot
from move_action import MoveAction
from rotate_action import RotateAction
from navigate_action import NavigateAction
from figure_8_action import Figure8Action
from move_random_action import MoveRandomAction
from move_to_random_point_action import MoveToRandomPointAction
from math import pi

rospy.init_node('main')

robot = Robot('robot_0', 3, 0.5, 0, 0, pi/2)
robot1 = DifferentRobot('robot_1', 2, 0.5, 0, 0, pi/2)
animal = Animal('robot_2', 2, 2, 0, 0, pi/2)
person = Robot('robot_3', 2, 0.5, -17, 37, 0)

robot.add_action(MoveAction(75))
robot.add_action(RotateAction("rotate_to_east"))
robot.add_action(MoveAction(3.5))
robot.add_action(RotateAction("rotate_to_south"))
robot.add_action(MoveAction(75))
robot.add_action(RotateAction("rotate_to_west"))
robot.add_action(MoveAction(3.5))
robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(MoveAction(75))

#robot1.add_action(Figure8Action())
animal.add_action(MoveToRandomPointAction())

# robot1.add_action(NavigateAction(50, 50))
# animal.add_action(NavigateAction(50, 50))
person.add_action(NavigateAction(15, 15))

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()
    animal.execute()
    person.execute()

    rate.sleep()
