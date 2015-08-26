#!/usr/bin/env python
import sys
import unittest
import rospy

from robots import Robot
from math import pi
import robot_storage

PKG = 'speedkiwi_test'


class TestRobotStorage(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_robot_storage')
        self.robot_obj = Robot('robot_0', 2, 0.9, -20, 43, 0)


    def test_add_robot(self):
        """test add robot method"""
        robot_storage.addRobot(self.robot_obj, self.robot_obj.robot_id)
        test_list = robot_storage.get_robot_list()
        self.assertIn(self.robot_obj.robot_id, test_list)

    def test_get_robot_with_id(self):
        """Test get robot with id method returns robot"""
        robot_storage.addRobot(self.robot_obj, self.robot_obj.robot_id)
        result = robot_storage.getRobotWithId(self.robot_obj.robot_id)
        self.assertEqual(result, self.robot_obj)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_robot_storage', TestRobotStorage, sys.argv)
