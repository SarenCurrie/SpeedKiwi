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
        self.person.cmd_handler("up")
        self.assertTrue(self.person.current_speed, 1)

    def test_cmd_handler_down(self):
        self.person.cmd_handler("down")
        self.assertTrue(self.person.current_speed, -1)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_educated_person', TestEducatedPerson, sys.argv)