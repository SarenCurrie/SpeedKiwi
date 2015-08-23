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
		#rospy.loginfo("Move: %s", str(data.data))
		msg = str(data.data)
		if msg == 'up':
			rospy.loginfo("Move up")
			self.current_speed = self.top_speed
			self.forward()
		elif msg == 'down':
			rospy.loginfo("Move down")
			self.current_speed = -self.current_speed
			self.forward()
		elif msg == 'left':
			rospy.loginfo("Move left")
			self.stop()
			self.start_rotate()
		elif msg == 'right':
			rospy.loginfo("Move right")
			self.stop()
			self.start_rotate_opposite()
