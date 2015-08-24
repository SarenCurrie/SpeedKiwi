#!/usr/bin/env python

import rospy
from robots import Robot, Animal, Person, DifferentRobot, PickerRobot, Bin, Tractor, EducatedPerson
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction
import robot_storage
from math import pi



rospy.init_node('main')

# Please for the love of God do not move these around - they get built at run time
animal = Animal('robot_0', 2, 0.5, 19, -45, 0)

person1 = Person('robot_1', 2, 0.5, 0, 40, 0)
person2 = EducatedPerson('robot_2', 2, 0.5, 27, -48, 0)

tractor = Tractor('robot_3', 2, 0.9, -20, 43, 0)

binbot1 = Bin('robot_4', 3, 0.5, -8.75, -38, pi/2)
binbot2 = Bin('robot_5', 3, 0.5, -1.75, -38, pi/2)
binbot3 = Bin('robot_6', 3, 0.5, 1.75, -38, pi/2)
binbot4 = Bin('robot_7', 3, 0.5, 8.75, -38, pi/2)

picker1 = PickerRobot('robot_8', 3, 0.5, -8.75, -41, 0)
picker2 = PickerRobot('robot_9', 3, 0.5, 1, -41, 0)
picker3 = PickerRobot('robot_10', 3, 0.5, 5, -43, 0)

robot = Robot('robot_11', 3, 0.5, -8.5, -37, 0)  # Will be carrier #1
robot1 = DifferentRobot('robot_12', 2, 0.5, 0, 0, 0)  # Will be carrier #2

robot_storage.addRobot(animal, "robot_0")
robot_storage.addRobot(person1, "robot_1")
robot_storage.addRobot(person2, "robot_2")
robot_storage.addRobot(tractor, "robot_3")
robot_storage.addRobot(binbot1, "robot_4")
robot_storage.addRobot(binbot2, "robot_5")
robot_storage.addRobot(binbot3, "robot_6")
robot_storage.addRobot(binbot4, "robot_7")
robot_storage.addRobot(picker1, "robot_8")
robot_storage.addRobot(picker2, "robot_9")
robot_storage.addRobot(picker3, "robot_10")
robot_storage.addRobot(robot, "robot_11")
robot_storage.addRobot(robot1, "robot_12")

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()
    animal.execute()
    tractor.execute()
    person1.execute()
    person2.execute()
    binbot1.execute()
    binbot2.execute()
    binbot3.execute()
    binbot4.execute()
    picker1.execute()
    picker2.execute()
    picker3.execute()
    tractor.execute()

    rate.sleep()
