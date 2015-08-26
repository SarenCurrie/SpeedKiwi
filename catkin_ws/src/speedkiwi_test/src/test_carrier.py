#!/usr/bin/env python
import sys
import unittest
import rospy
from actions import NavigateAction, MoveAction, RotateAction
from world_locations import locations
from robots import Robot, CarrierRobot
from math import pi

PKG = 'speedkiwi_test'


class TestPicker(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_picker')
        self.picker = CarrierRobot('robot_0', 2, 0.9, -20, 43, 0)

    def test_init(self):
        """Checks if subscribed information has been received."""
        self.assertIsNot(self.picker.odometry, None)
        self.assertIsNot(self.picker.leftLaser, None)
        self.assertIsNot(self.picker.rightLaser, None)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_carrier', TestCarrier, sys.argv)
