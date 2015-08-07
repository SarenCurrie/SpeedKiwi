#!/usr/bin/env python

import Robot
import rospy

rospy.init_node('test')
robot = Robot.Robot('robot_0', 0.5, 0.5, 0, 0, 0)
robot2 = Robot.Robot('robot_1', 0.5, 0.5, 0, 0, 0)

robot.forward()
robot2.stop()

rate = rospy.Rate(10)

frequency = 50
counter = 0

while not rospy.is_shutdown():
    robot.execute()
    robot2.execute()
    
    counter += 1

    if (counter % frequency == 0) and not (counter % (2 * frequency) == 0):
        robot.stop()
        robot2.forward()

    if counter % (2 * frequency) == 0:
        robot.forward()
        robot2.stop()
    
    rate.sleep()
