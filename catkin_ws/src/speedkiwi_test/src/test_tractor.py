#!/usr/bin/env python
import sys
import unittest
import rospy
from actions import NavigateAction, MoveAction, RotateAction
from world_locations import locations
from robots import Robot, Tractor
from math import pi

PKG = 'speedkiwi_test'


class TestTractor(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_tractor')
        self.tractor = Tractor('robot_0', 2, 0.9, -20, 43, 0)

    def test_init(self):
        """Checks if subscribed information has been received."""
        self.assertIsNot(self.tractor.odometry, None)
        self.assertIsNot(self.tractor.leftLaser, None)
        self.assertIsNot(self.tractor.rightLaser, None)

    def test_execute_callback_was_blocked_false(self):
        """Test actions are added to queue when was_blocked is false"""
        self.tractor.was_blocked = False
        self.tractor._action_queue[:] = [] #clear the list
        self.tractor.execute_callback()
        self.assertEqual(len(self.tractor._action_queue),4)

    def test_execute_callback_was_blocked_true(self):
        """test was_blocked is true and action queue is old 
        queue when was_blocked is true"""
        self.tractor.was_blocked = True
        self.tractor.old_queue = []
        self.tractor.execute_callback()
        self.assertFalse(self.tractor.was_blocked)
        self.assertEqual(self.tractor._action_queue,self.tractor.old_queue)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_tractor', TestTractor, sys.argv)
