import rospy
from std_msgs.msg import String

class EducatedPerson(object):

	def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
		Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
		self.type = type(self).__name__
		rospy.Subscriber("move_command", String, cmd_handler)

	def cmd_handler(data):
		rospy.loginfo("Move: ", data.data)
