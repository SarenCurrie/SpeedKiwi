from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import random
import rospy

from Robot import Robot
from MoveAction import MoveAction
from RotateAction import RotateAction

class Animal(Robot):
	"""Subclass of Robot which implements random movement"""
	def __init__(self, name):
		Robot.__init__(self,name, 100, 3, 1, 1, 0)

	def execute_callback(self):
		"""Behaviour: run around in circles."""
		randint = random.randint(1,5)

		if 1 <= randint <= 4:
			self.forward()
		else:
			self.start_rotate()

