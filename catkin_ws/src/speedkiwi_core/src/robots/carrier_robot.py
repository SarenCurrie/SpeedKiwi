from robots import Robot
import rospy
import os
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status
from actions import MoveAction, RotateAction, NavigateAction, Figure8Action, MoveRandomAction
import random
from std_msgs.msg import String
import math
import random

class CarrierRobot(Robot):
	def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

    def execute_callback(self):
    	"""Logic for the carrier robot"""
    	randint = random.randint(1,2)
    	if randint == 1:
    		self.add_action(RotateAction("rotate_to_south"))
    	else:
    		self.add_action(RotateAction("rotate_to_north"))
