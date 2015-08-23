#!/usr/bin/env python

import rospy
from robots import Robot, Animal, Person, DifferentRobot, PickerRobot, Bin, Tractor, EducatedPerson
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction
from math import pi

rospy.init_node('main')

animal = Animal('robot_0', 2, 2, 19, -45, 0)

person1 = Person('robot_1', 2, 0.5, 0, 40, 0)
person2 = EducatedPerson('robot_2', 2, 0.5, 27, -48, 0)

tractor = Tractor('robot_3', 2, 2, -20, 43, 0)

binbot1 = Bin('robot_4',3, 0.5, -8.75, -38, 0)
binbot2 = Bin('robot_5',3, 0.5, -8.75, -38, 0)
binbot3 = Bin('robot_6',3, 0.5, -8.75, -38, 0)
binbot4 = Bin('robot_7',3, 0.5, -8.75, -38, 0)

picker1 = PickerRobot('robot_8', 3, 0.5, -8.75, -41, 0)
picker2 = PickerRobot('robot_9', 3, 0.5, 1, -41, 0)
picker3 = PickerRobot('robot_10', 3, 0.5, 5, -43, 0)

robot = Robot('robot_11', 3, 0.5, -8.5, -37, 0) #Will be carrier #1
robot1 = DifferentRobot('robot_12', 2, 0.5, 0, 0, 0) #Will be carrier #2


# Testing bin mimicking:
binbot1.latch(picker1)
picker1.add_slave(binbot1)

# robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(MoveAction(1))
robot.add_action(RotateAction("rotate_to_west"))
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
    person1.execute()
    person2.execute()
    binbot1.execute()
    binbot2.execute()
    binbot3.execute()
    binbot4.execute()
    picker1.execute()
    picker2.execute()
    picker3.execute()


    rate.sleep()
