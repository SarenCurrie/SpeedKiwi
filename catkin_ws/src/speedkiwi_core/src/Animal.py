from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import random
import rospy

from Robot import Robot

class Animal(Robot):
	def __init__(self, name):
		Robot.__init__(self,name, 100, 3, 1, 1, 0)

	def forward(self):
		self.set_velocity(random.random()*10)

	def execute_callback(self):
		self.set_velocity(random.random()*10)
	
