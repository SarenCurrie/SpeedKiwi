#!/usr/bin/env python

import rospy
from robots import Robot, Animal, Person, DifferentRobot, PickerRobot, CarrierRobot, Bin, Tractor, EducatedPerson
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction
import robot_storage
from math import pi


"""Main file for initializing and executing the robots of the orchard simulator."""
rospy.init_node('main')

# Construction of robots.
# NOTE: PLEASE for the love of GOD do not move these around - they get built at run time.
animal = Animal('robot_0', 2, 0.5, 20.5, 0, 0)

person1 = Person('robot_1', 2, 0.5, 0, 45, 0)
person2 = EducatedPerson('robot_2', 2, 0.5, -20.5, 0, 0)

tractor = Tractor('robot_3', 2, 0.9, -20.5, 45, 0)

binbot1 = Bin('robot_4', 3, 0.5, -8.75, -39, pi/2)
binbot2 = Bin('robot_5', 3, 0.5, -1.75, -39, pi/2)
binbot3 = Bin('robot_6', 3, 0.5, 1.75, -39, pi/2)
binbot4 = Bin('robot_7', 3, 0.5, 5.25, -39, pi/2)

picker1 = PickerRobot('robot_8', 3, 0.5, -8.75, -44, 0)
picker2 = PickerRobot('robot_9', 3, 0.5, 1, -44, 0)
picker3 = PickerRobot('robot_10', 3, 0.5, 7, -44, 0)

carrier1 = CarrierRobot('robot_11', 3, 0.5, 35.5, -25, 0)
carrier2 = CarrierRobot('robot_12', 2, 0.5, 41.5, -35, 0)

# Add all robots to robot_storage.
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
robot_storage.addRobot(carrier1, "robot_11")
robot_storage.addRobot(carrier2, "robot_12")

rate = rospy.Rate(10)

# Continually execute robots in execution loop
while not rospy.is_shutdown():

    animal.execute()
    tractor.execute()
    person1.execute()
    person2.execute()
    picker1.execute()
    picker2.execute()
    picker3.execute()
    binbot1.execute()
    binbot2.execute()
    binbot3.execute()
    binbot4.execute()
  #  carrier1.execute()
  #  carrier2.execute()
    
    rate.sleep()
