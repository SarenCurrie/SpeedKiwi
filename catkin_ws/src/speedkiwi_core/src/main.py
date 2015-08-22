#!/usr/bin/env python

import rospy
from robots import Robot, Animal, Person, DifferentRobot, PickerRobot, Bin
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction,MoveToRandomPointAction
from math import pi

rospy.init_node('main')

robot = PickerRobot('robot_0', 3, 0.5, -8.5, -37, 0)
robot1 = DifferentRobot('robot_1', 2, 0.5, 0, 0, pi/2)
animal = Animal('robot_2', 2, 2, 0, 0, pi/2)
person = Robot('robot_3', 2, 0.5, -17, 37, 0)
kiwi_bin = Bin('robot_6', 3, 0.5, 0, -40, 0)
picker = PickerRobot('robot_9', 3, 0.5, 0, -45, 0)

# robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(MoveAction(1))
robot.add_action(RotateAction("rotate_to_north"))
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
    kiwi_bin.execute()
    picker.execute()

    rate.sleep()
