from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import rospy
from robot import Robot
from move_action import MoveAction
from rotate_action import RotateAction


class Animal(Robot):
    """Subclass of Robot which implements random movement"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__
