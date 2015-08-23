from robots import Robot
from std_msgs.msg import String
from speedkiwi_msgs.msg import bin_status, empty_response
import rospy

class Bin(Robot):
    """Class for bins of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

        # Unique booleans for Bin instance
        self.is_publishing = True
        self.is_empty = True
        self.is_latched = False

        self.master = None

        def id_response(data):
            # If recieves bin recieves own id back, set latched to true

            # rospy.loginfo("Data: %s - Self: %s", data.bin_id, self.robot_id)

            if data.bin_id == self.robot_id:
                self.is_publishing = False

        # Suscribe to topic to recieve response from pickers.
        rospy.Subscriber("empty_response_topic", empty_response, id_response)

    def execute_callback(self):
        """Logic for Bin"""

        bin_pub = rospy.Publisher('bin_status_topic', bin_status, queue_size=10)

        if self.is_publishing:
        	# Publish message bin's details to let pickers know that it can be picked up.
            msg = bin_status()
            msg.bin_id = self.robot_id
            msg.x = self.position["x"]
            msg.y = self.position["y"]
            bin_pub.publish(msg)
<<<<<<< Updated upstream


=======
       
>>>>>>> Stashed changes
    def latch(self, robot):
        self.master = robot
