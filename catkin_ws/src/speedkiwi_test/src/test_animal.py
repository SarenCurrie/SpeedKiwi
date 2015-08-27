#!/usr/bin/env python
import sys
import unittest
import rospy

from robots import Animal, PickerRobot
from speedkiwi_msgs.msg import robot_status

PKG = 'speedkiwi_test'


class TestAnimal(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_animal')
        self.animal = Animal('robot_0', 2, 0.5, 0, 0, 0)

    def test_init(self):
        """Checks if animal attributes are set correctly after init."""
        animal = self.animal
        self.assertFalse(animal.currently_targeting)
        self.assertEqual(animal.dict_index, -1)
        self.assertEqual(animal.counter, 0)
        self.assertFalse(animal.retreat, False)

    def test_dog_stops_retreating(self):
        """Check the dog stops retreating when it reaches the kennel"""
        animal = self.animal
        animal.retreat = True
        animal.execute_callback()
        self.assertFalse(animal.retreat)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_animal', TestAnimal, sys.argv)