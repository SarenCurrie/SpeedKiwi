#!/usr/bin/env python
import sys
import unittest
import rospy
from actions import NavigateAction, MoveAction, RotateAction
from world_locations import locations
from robots import Robot, CarrierRobot
from math import pi

PKG = 'speedkiwi_test'


class TestCarrier(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_picker')
        self.carrier = CarrierRobot('robot_0', 2, 0.9, -20, 43, 0)

    def test_execute_callback_speed(self):
        """Checks carrier sets speed to top speed in execute_callback"""
        self.carrier.current_speed = 0
        self.carrier.execute_callback()
        self.assertEqual(self.carrier.current_speed, self.carrier.top_speed)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_carrier', TestCarrier, sys.argv)
