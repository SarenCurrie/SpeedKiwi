#!/usr/bin/env python

from Robot import Robot
from DifferentRobot import DifferentRobot
from MoveAction import MoveAction
from RotateAction import RotateAction
import rospy

rospy.init_node('test')
robot = Robot.Robot('robot_0', 0.5, 0.5, 0 , 0, 0)

robot.add_action(RotateAction("rotate_to_south"))
robot.add_action(RotateAction("rotate_to_north"))
robot.add_action(RotateAction("rotate_to_east"))
robot.add_action(MoveAction(5))
robot.add_action(RotateAction("rotate_to_west"))
robot.add_action(MoveAction(10))
robot1.forward()

rate = rospy.Rate(10)

counter = 0

while not rospy.is_shutdown():
    robot.execute()
    robot1.execute()

    rate.sleep()
