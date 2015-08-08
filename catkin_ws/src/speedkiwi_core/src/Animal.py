from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import random
import rospy

from Robot import Robot

class Animal(Robot):
	"""Subclass of Robot which implements random movement"""
	def __init__(self, name):
		Robot.__init__(self,name, 100, 3, 1, 1, 0)

	def execute_callback(self):
		self.set_velocity(random.random())
		# TODO: Change direction randomly.
	
