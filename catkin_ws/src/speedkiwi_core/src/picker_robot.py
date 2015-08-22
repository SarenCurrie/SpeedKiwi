from robot import Robot
from speedkiwi_core.msg import empty_response

class PickerRobot(Robot):
    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

        rospy.Subscriber("bin_status", String, callback)

        def callback(data):
            if self.is_closest == 1:
                self.current_bin_x = data.x
                self.current_bin_y = data.y

                empty_response_pub = rospy.Publisher('empty_response_topic', String, queue_size=10)
                rate = rospy.Rate(10)

                msg = empty_response()
                msg.picker_id = self.robot_id
                msg.bin_id = data.robot_id

                empty_response_pub.publish(msg)
                rate.sleep()

    def execute_callback(self):
        """Logic for the picker robot."""

    def is_closest(self):
        """Check if this picker is the closest to the specified bin."""
        return 1