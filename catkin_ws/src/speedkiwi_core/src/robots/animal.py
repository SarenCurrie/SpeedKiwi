from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import rospy
from robot import Robot
from actions import MoveAction, RotateAction, NavigateAction
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status
import random

class Animal(Robot):
    """Subclass of Robot which implements random movement"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__
        self.robot_dict = dict()
        self.currently_targeting = False
        self.target = robot_status
        self.dict_index = -1
        def robot_locations(data):
        	if data.robot_type == "PickerRobot" or data.robot_type == "CarrierRobot":
        		self.robot_dict[data.robot_id] = data
        
        rospy.Subscriber("statuses", robot_status, robot_locations)

    def execute_callback(self):
    	"""Logic for the animal"""
    	if not self.currently_targeting:
    		if bool(self.robot_dict):
	    		#pick a random robot from dict to target
	    		self.dict_index = random.randint(0,len(self.robot_dict)-1)
	    		self.currently_targeting = True
		if self.dict_index is not -1:
			target_x = self.robot_dict.values()[self.dict_index].x
			target_y = self.robot_dict.values()[self.dict_index].y
			target_id = self.robot_dict.values()[self.dict_index].robot_id
			rospy.loginfo(self.robot_id + " targeting " + str(target_id) + " at " + str(target_x) + "," + str(target_y))



