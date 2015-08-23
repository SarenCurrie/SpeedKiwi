#!/usr/bin/env python

import rospy
from robots import Robot, Animal, Person, DifferentRobot, PickerRobot, Bin, Tractor
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction
from math import pi

rospy.init_node('main')

robot = Robot('robot_0', 3, 0.5, -8.5, -37, pi/2)
robot1 = DifferentRobot('robot_1', 2, 0.5, 0, 0, pi/2)
animal = Animal('robot_2', 2, 2, 0, 0, pi/2)
person = Robot('robot_3', 2, 0.5, -17, 37, 0)
tractor = Tractor('robot_5', 6, .5, -20, -45, 0)
binbot = Bin('robot_6',3, 0.5, -8.5, -37, pi/2)
picker2 = PickerRobot('robot_9', 3, 0.5, 0, -45, 0)
picker3 = PickerRobot('robot_10', 3, 0.5, 5, -40, 0)

# Testing bin mimicking:
binbot.latch(robot)
robot.add_slave(binbot)

# # robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(MoveAction(1))
robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(MoveAction(78))
robot.add_action(RotateAction("rotate_to_east"))
robot.add_action(MoveAction(3.5))
robot.add_action(RotateAction("rotate_to_south"))
robot.add_action(MoveAction(78))
robot.add_action(RotateAction("rotate_to_west"))
robot.add_action(MoveAction(3.5))

#robot1.add_action(Figure8Action())
animal.add_action(NavigateAction(0, 40))

# robot1.add_action(NavigateAction(50, 50))
# animal.add_action(NavigateAction(50, 50))
# person.add_action(NavigateAction(15, 15))

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()
    animal.execute()
    person.execute()
    binbot.execute()
    picker2.execute()
    picker3.execute()
    tractor.execute()

    rate.sleep()
