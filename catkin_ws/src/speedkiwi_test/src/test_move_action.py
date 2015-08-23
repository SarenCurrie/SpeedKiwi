#!/usr/bin/env python
import sys
import unittest
import rospy

from actions import MoveAction
from robots import Robot
from math import pi

PKG = 'speedkiwi_test'

class TestMoveAction(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_move_action')
        self.robot = Robot('robot_0', 1, 0.5, 1, 1, pi/2)
        self.robot1 = Robot('robot_0', 1, 0.5, 0, 0, pi/2)

    def test_init(self):
        """Checks if distance is set correctly after initialising."""
        action = MoveAction(5)
        self.assertEqual(action.distance, 5)

    def test_start(self):
        """Checks if starting positions are set from robot."""
        action = MoveAction(5)
        action.start(self.robot)

        self.assertEqual(action.x_start, 1)
        self.assertEqual(action.y_start, 1)

    def test_is_finished(self):
        """Checks if MoveAction correctly detects that it's finished."""
        action = MoveAction(5)
        self.robot.odometry.pose.pose.position.x = 5
        self.robot.odometry.pose.pose.position.y = 5

        self.assertTrue(action.is_finished(self.robot))

    def test_is_not_finished(self):
        """Checks if MoveAction correctly detects that it's not finished."""
        action = MoveAction(5)
        self.robot.odometry.pose.pose.position.x = 3
        self.robot.odometry.pose.pose.position.y = 2

        self.assertFalse(action.is_finished(self.robot))

    def to_string(self):
        return "test movement"

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_move_action', TestMoveAction, sys.argv)
