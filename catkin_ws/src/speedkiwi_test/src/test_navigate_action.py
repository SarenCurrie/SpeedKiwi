#!/usr/bin/env python
import sys
import unittest
import rospy

from actions import NavigateAction
from robots import Robot
from math import pi

PKG = 'speedkiwi_test'

class TestNavigateAction(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_move_action')
        self.robot = Robot('robot_0', 1, 0.5, 1, 1, pi/2)

    def test_init(self):
        """Checks if target is set correctly after initialising."""
        action = NavigateAction(15, 16)
        self.assertEqual(action.x_target, 15)
        self.assertEqual(action.y_target, 16)

    def test_start(self):
        """Checks if starting positions are set from robot."""
        action = NavigateAction(15, 16)
        action.start(self.robot)

        self.assertEqual(action.x_start, 1)
        self.assertEqual(action.y_start, 1)

    def test_is_finished(self):
        """Checks if MoveAction correctly detects when it's not finished."""
        action = NavigateAction(15, 16)
        self.robot.odometry.pose.pose.position.x = 15.5
        self.robot.odometry.pose.pose.position.y = 16.49

        self.assertFalse(action.is_finished(self.robot))

    def test_is_not_finished(self):
        """Checks if MoveAction correctly detects that it's not finished."""
        action = NavigateAction(15, 16)
        self.robot.odometry.pose.pose.position.x = 15
        self.robot.odometry.pose.pose.position.y = 15.49

        self.assertFalse(action.is_finished(self.robot))

    def to_string(self):
        return "test movement"

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_navigate_action', TestNavigateAction, sys.argv)
