import rospy
from std_msgs.msg import String
from robots import Robot

class EducatedPerson(Robot):

	def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
		Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
		self.type = type(self).__name__
		self.command = None
		rospy.Subscriber("move_command", String, self.cmd_handler)

	def cmd_handler(self, data):
		rospy.loginfo("Move: %s", str(data.data))
		


