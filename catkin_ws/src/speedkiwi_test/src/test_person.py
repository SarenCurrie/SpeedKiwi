#!/usr/bin/env python
import sys
import unittest
import rospy

from robots import Person
from world_locations import locations

PKG = 'speedkiwi_test'


class TestPerson(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_person')
        self.person = Person('robot_0', 2, 0.5, 0, 0, 0)
        self.boundaries = locations.get_orchard_boundaries()

    def test_init(self):
        """Checks if attributes are set correctly after init.
        Values are based on world_locations files."""
        person = self.person
        self.assertEquals(person.counter, 0)
        self.assertEquals(person.min_x, -35)
        self.assertEquals(person.max_x, 35)
        self.assertEquals(person.min_y, -60)
        self.assertEquals(person.max_y, 60)

    def test_execute_callback(self):
        """Checks to see if action queue has action and
        counter has incremented accordingly."""
        self.person.execute_callback()
        self.assertEquals(self.person.counter, 1)
        self.assertIsNot(len(self.person._action_queue), 0)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_person', TestPerson, sys.argv)