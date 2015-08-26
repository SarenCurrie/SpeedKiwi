import rospy
from std_msgs.msg import String
from robots import Robot


class EducatedPerson(Robot):
    """Class representing a person with intelligence.
    Controlled by arrow keys on keyboard. Use with person_controller.py.
    """
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__
        self.command = None
        rospy.Subscriber("move_command", String, self.cmd_handler)

    def cmd_handler(self, data):
        """Gets the published arrow key input and moves the person accordingly."""
        # rospy.loginfo("Move: %s", str(data.data))
        msg = str(data.data)
        if msg == 'up':
            rospy.loginfo("Educated person is moving up")
            self.current_speed = self.top_speed
            self.forward()
        elif msg == 'down':
            rospy.loginfo("Educated person is moving down")
            self.current_speed = -self.current_speed
            self.forward()
        elif msg == 'left':
            rospy.loginfo("Educated person is moving left")
            self.stop()
            self.start_rotate()
        elif msg == 'right':
            rospy.loginfo("Educated person is moving right")
            self.stop()
            self.start_rotate_opposite()
