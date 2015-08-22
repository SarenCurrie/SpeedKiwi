from robot import Robot
from std_msgs.msg import String
from speedkiwi_core.msg import bin_status
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

        # Suscribe to topic to recieve response from pickers.
        rospy.Subscriber("empty_response_topic", String, id_response)

        def id_response(data):
            rospy.loginfo("Compare id's: %s %s", data.robot_id, self.robot_id)

            # If recieves bin recieves own id back, set latched to true
            if data.robot_id is self.robot_id: # Is this right?
                self.is_publishing = False


    def execute_callback(self):
        """Logic for Bin"""

        bin_pub = rospy.Publisher('bin_status', String, queue_size=10)
        rate = rospy.Rate(10)

        while self.is_publishing:
        	# Publish message bin's details to let pickers know that it can be picked up.
            msg = bin_status()
            msg.robot_id = self.robot_id
            msg.x = self.position["x"]
            msg.y = self.position["y"]
        	bin_pub.publish(msg)
        	rate.sleep()
       


    def latch(self, robot):
        self.master = robot


    def mimic(self):
        self.add_action(self.master.current_action())
