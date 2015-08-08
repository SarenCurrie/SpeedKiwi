from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
from random import randint
import rospy

from Robot import Robot

class Animal(Robot):
	"""Subclass of robot which implements random movement."""
	def __init__(self, name):
		Robot.__init__(self, name, 100, 3, 1, 1, 0)

	def execute_callback(self):
		self.forward()
		rospy.loginfo('Before time sleep')
		time.sleep(random.randint(3,6))
		rospy.loginfo('After time sleep')
		self.stop()
	
