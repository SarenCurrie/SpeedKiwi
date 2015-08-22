#!/usr/bin/env python
import sys
import unittest
import rospy

from robot import Robot
from math import pi

PKG = 'speedkiwi_core'


class TestRobot(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_move_action')
        self.robot = Robot('robot_0', 1, 0.5, 1, 1, pi / 2)

    def test_init(self):
        """Checks if subscribed information has been received."""
        self.assertIsNot(self.robot.odometry, None)
        self.assertIsNot(self.robot.leftLaser, None)
        self.assertIsNot(self.robot.rightLaser, None)

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

    def test_set_angular_velocity(self):
        """Checks if angular velocity is set to the specified value."""
        self.robot.set_angular_velocity(0.2)
        self.assertEqual(self.robot.velocity.angular.z, 0.2)

    def test_set_linear_velocity(self):
        """Checks if linear velocity is set to the specified value."""
        self.robot.set_linear_velocity(0.7)
        self.assertEqual(self.robot.velocity.linear.x, 0.7)

    def test_start_rotate(self):
        """Checks if angular velocity is set to angular_top_speed
        and rotation_executing is set to true."""
        self.robot.start_rotate()

        self.assertEqual(self.robot.velocity.angular.z, 0.5)
        self.assertTrue(self.robot.rotation_executing)

    def test_start_rotate_opposite(self):
        """Checks if angular velocity is set to angular_top_speed in the
        negative direction and rotation_executing is set to true."""
        self.robot.start_rotate_opposite()

        self.assertEqual(self.robot.velocity.angular.z, -0.5)
        self.assertTrue(self.robot.rotation_executing)

    def test_stop_rotate(self):
        """Checks to see if angular velocity is set to 0 and
        rotation_executing is set to false."""
        self.robot.stop_rotate()

        self.assertEqual(self.robot.velocity.angular.z, 0)
        self.assertFalse(self.robot.rotation_executing)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_robot', TestRobot, sys.argv)
