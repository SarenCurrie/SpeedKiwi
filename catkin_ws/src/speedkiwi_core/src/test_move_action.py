#!/usr/bin/env python
import sys
import unittest
from move_action import MoveAction
from robot import Robot
from math import pi
import rospy

PKG = 'speedkiwi_core'

class TestMoveAction(unittest.TestCase):

	def test_init(self):
		"""Checks if distance is set correctly after initialising."""
		action = MoveAction(5)
		self.assertEqual(action.distance, 5)

if __name__ == '__main__':
	import rostest
	rostest.rosrun(PKG, 'test_move_action', TestMoveAction, sys.argv)
