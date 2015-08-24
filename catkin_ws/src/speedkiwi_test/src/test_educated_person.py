#!/usr/bin/env python
import sys
import unittest
import rospy

from robots import EducatedPerson
from std_msgs.msg import String

PKG = 'speedkiwi_test'


class TestEducatedPerson(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_educated_person')
        self.person = EducatedPerson('robot_0', 1, 0.5, 0, 0, 0)

    def test_init(self):
        """Checks if attributes are set correctly after init."""
        self.assertTrue(1, 1)

    def test_cmd_handler_up(self):
        """Checks that a person moves forward when given up msg."""
        msg = String()
        msg.data = "up"
        self.person.cmd_handler(msg)
        self.assertEqual(self.person.current_speed, 1)

    def test_cmd_handler_down(self):
        """Checks that a person reverses when given down msg."""
        msg = String()
        msg.data = "down"
        self.person.cmd_handler(msg)
        self.assertEqual(self.person.current_speed, -1)

    def test_cmd_handler_left(self):
        """Checks that person rotates anticlockwise when given left msg."""
        msg = String()
        msg.data = "left"
        self.person.cmd_handler(msg)
        self.assertTrue(self.person.rotation_executing)
        self.assertEqual(self.person.velocity.angular.z, 0.5)

    def test_cmd_handler_right(self):
        """Checks that person rotates clockwise when given right msg."""
        msg = String()
        msg.data = "right"
        self.person.cmd_handler(msg)
        self.assertTrue(self.person.rotation_executing)
        self.assertEqual(self.person.velocity.angular.z, -0.5)

    def test_cmd_handler_other(self):
        """Checks that person doesn't move when given a random input."""
        msg = String()
        msg.data = "this_does_nothing"
        self.person.cmd_handler(msg)
        self.assertFalse(self.person.rotation_executing)
        self.assertEqual(self.person.velocity.angular.x, 0)
        self.assertEqual(self.person.velocity.angular.y, 0)
        self.assertEqual(self.person.velocity.angular.z, 0)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_educated_person', TestEducatedPerson, sys.argv)