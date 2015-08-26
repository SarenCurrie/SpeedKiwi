#!/usr/bin/env python
import sys
import unittest
import rospy
from actions import NavigateAction, MoveAction, RotateAction
from world_locations import locations
from robots import Robot, PickerRobot
from math import pi

PKG = 'speedkiwi_test'


class TestPicker(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_picker')
        self.picker = PickerRobot('robot_0', 2, 0.9, -20, 43, 0)

    def test_picker_count(self):
        """Test that the kiwifruit count increments when in orchard"""
        self.picker.position['x'] = 0
        self.picker.position['y'] = 0 #origin is in orchard
        self.picker.fruit_count = 0
        self.picker.execute_callback()
        if self.picker.randint == 1:
            self.assertEqual(self.picker.fruit_count,1)
        else:
            self.assertEqual(self.picker.fruit_count,0)

    def test_picker_picking_speed(self):
        """Check the picker slows down to its picking speed when in orchard"""
        self.picker.current_speed = 1
        self.picker.position['x'] = 0
        self.picker.position['y'] = 0 #origin is in orchard
        self.picker.execute_callback()
        self.assertEqual(self.picker.current_speed,self.picker.pick_speed)

    def test_picker_normal_speed(self):
        """Check the picker sets a normal speed when it's outside orchard"""
        self.picker.current_speed = self.picker.pick_speed
        self.picker.position['x'] = 9000
        self.picker.position['y'] = 9000 #position out of orchard
        self.picker.execute_callback()
        self.assertEqual(self.picker.current_speed, self.picker.top_speed)

    def test_check_full_true(self):
        """Test check_full method to see if it detects a full count"""
        self.picker.fruit_count = 999999999
        self.assertTrue(self.picker.check_full())

    def test_check_full_false(self):
        """Test check_full method to see if it detects non-full bin"""
        self.picker.fruit_count = 0
        self.assertFalse(self.picker.check_full())
if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_picker', TestPicker, sys.argv)
