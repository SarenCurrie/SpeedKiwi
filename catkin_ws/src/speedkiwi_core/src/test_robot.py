#!/usr/bin/env python
import sys
import unittest
import rospy

from move_action import MoveAction
from robot import Robot
from math import pi

PKG = 'speedkiwi_core'

class TestRobot(unittest.TestCase):

	def setUp(self):
		rospy.init_node('test_move_action')
		self.robot = Robot('robot_0', 1, 0.5, 1, 1, pi/2)
		self.robot1 = Robot('robot_0', 1, 0.5, 0, 0, pi/2)

#	def test_init(self):
		# TODO: Check subscriptions?		

	def test_forward(self):
		"""Checks if forward sets the velocity to its top speed."""
		self.robot.forward()
		self.assertEqual(self.robot.velocity.linear.x, 1)

	def test_stop(self):
		"""Checks if stop sets the linear and angular velocity to 0."""
		self.robot.forward()
		self.robot.start_rotate()
		self.robot.stop()

		self.assertEqual(self.robot.velocity.linear.x, 0)
		self.assertEqual(self.robot.velocity.angular.z, 0)

if __name__ == '__main__':
	import rostest
	rostest.rosrun(PKG, 'test_robot', TestRobot, sys.argv)
