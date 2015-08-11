#!/usr/bin/env python
PKG='speedkiwi_core'
import roslib; roslib.load_manifest(PKG)  # This line is not needed with Catkin.

import sys
import unittest

## A sample python unit test
class TestRobot(unittest.TestCase):

    def test_robot_initialisation(self):
            Robot.__init__(Robot, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)


if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'speedkiwi_core', TestRobot)