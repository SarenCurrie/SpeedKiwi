#!/usr/bin/env python

import Robot
import rospy

rospy.init_node('test')
robot = Robot.Robot('robot_0', 0.5, 0.5, 0 , 0, 0)

robot.forward()

rate = rospy.Rate(10)

counter = 0

while not rospy.is_shutdown():
    robot.execute()
    counter += 1

    if counter % 100 == 0 and not counter % 200 == 0:
        robot.stop()

    if counter % 200 == 0:
        robot.forward()

    rate.sleep()
