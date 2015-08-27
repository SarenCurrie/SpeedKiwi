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
        for i in range(0, 20):
            self.tractor.execute()

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

    def test_orchard_get_coordinates(self):
        """Test the boundary values obtained from file are floats
        NOTE: This is based on default world file. If configured world is run last this will fail"""
        boundaries = locations.get_wall_boundaries()
        self.tractor.min_x = boundaries["min_x"]
        self.tractor.max_x = boundaries["max_x"]
        self.tractor.min_y = boundaries["min_y"]
        self.tractor.max_y = boundaries["max_y"]
        self.assertEqual(self.tractor.min_x, -35)
        self.assertEqual(self.tractor.min_y, -60)
        self.assertEqual(self.tractor.max_x, 35)
        self.assertEqual(self.tractor.max_y, 60)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_tractor', TestTractor, sys.argv)
