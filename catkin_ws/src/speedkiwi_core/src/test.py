#!/usr/bin/env python

import Robot
import Animal
import rospy

rospy.init_node('test')
robot = Robot.Robot('robot_0', 0.5, 0.5, 1 , 1, 0)
robot2 = Animal.Animal('robot_1')

robot.forward()
robot2.forward()

rate = rospy.Rate(10)

counter = 0

while not rospy.is_shutdown():
    robot.execute()
    robot2.execute()
    counter += 1

    if counter % 100 == 0 and not counter % 200 == 0:
        robot.stop()

    if counter % 150 == 0 and not counter % 200 == 0:
        robot2.stop()

    if counter % 200 == 0:
        robot.forward()
        robot2.forward()

    rate.sleep()
