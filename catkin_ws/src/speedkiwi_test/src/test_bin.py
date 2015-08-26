#!/usr/bin/env python
import sys
import unittest
import rospy

from robots import Robot, Bin
from math import pi

PKG = 'speedkiwi_test'


class TestBin(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_bin')
        self.bin = Bin('robot_0', 1, 0.5, 1, 1, pi/2)
        self.robot = Robot('robot_1', 1, 0.5, 1, 1, pi/2)
        

    def test_init(self):
        """Checks that bin attributes are correctly initialised."""
        self.assertEquals(self.bin.slow_down_counter, 0)
        self.assertTrue(self.bin.is_publishing, True)
        self.assertTrue(self.bin.is_empty, True) 
        self.assertFalse(self.bin.is_carried, False)
        self.assertIsNone(self.bin.designated_picker)
        self.assertIsNone(self.bin.master)
        self.assertIsNone(self.bin.should_face)
        self.assertIsNotNone(self.bin.bin_latch)

    def test_latch_sets_master(self):
        """Checks that the latch function sets the bin's master to robot."""
        self.bin.latch(self.robot)
        self.assertEquals(self.bin.master.robot_id, self.robot.robot_id)

    def test_latch_stops_robot(self):
        """Checks that the latch function stops the robot it latches to."""
        self.bin.latch(self.robot)
        self.assertEquals(self.robot.velocity.linear.x, 0)
        self.assertFalse(self.robot.rotation_executing, False)

    def test_latch_sets_should_face(self):
        """Checks if latch function sets the should_face attribute."""
        self.bin.latch(self.robot)
        self.assertEquals(self.bin.should_face, pi/2)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_bin', TestBin, sys.argv)
