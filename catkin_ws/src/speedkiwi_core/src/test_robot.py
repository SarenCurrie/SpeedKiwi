#!/usr/bin/env python
import sys
import unittest
from robot import Robot
from math import pi


## A sample python unit test
class TestRobot(unittest.TestCase):

    def test_forward(self):
    	assert 1 == 1

if __name__ == '__main__':
	unittest.main()