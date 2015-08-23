#!/usr/bin/env python
import sys
import unittest
import rospy
import time

from actions import NavigateAction
from speedkiwi_msgs.msg import robot_status
from robots import Robot
from math import pi

PKG = 'speedkiwi_test'


class TestStatus(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_status')
        self.robot = Robot('robot_0', 1, 0.5, 1, 1, pi/2)
        self.robot1 = Robot('robot_1', 1, 0.5, 5, 5, pi/2)

        # Execute robots a few times to allow statuses to become existant.
        for i in range(0, 10):
            self.robot.execute()
            self.robot1.execute()
            time.sleep(0.1)

    def test_init(self):
        """Checks if status exists after initialising."""
        self.assertIsNotNone(self.robot.curr_robot_messages)
        self.assertIsNotNone(self.robot.curr_robot_messages[1])
        self.assertIsNotNone(self.robot.curr_robot_messages[1].robot_id)

    def test_robot_id(self):
        """Tests that the robots are publishing the correct id"""
        self.assertEquals(self.robot.curr_robot_messages[1].robot_id, 'robot_1')

    def test_position(self):
        """Tests whether the robots are publishing the correct position"""
        self.assertAlmostEqual(self.robot.curr_robot_messages[1].x, 5.0, places=2)

    def to_string(self):
        return "test movement"

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_status', TestStatus, sys.argv)
