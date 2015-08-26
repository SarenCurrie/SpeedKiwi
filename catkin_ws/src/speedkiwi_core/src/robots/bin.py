from robots import Robot
from std_msgs.msg import String
from speedkiwi_msgs.msg import bin_status, empty_response, full_response, robot_status
import robot_storage
import rospy


class Bin(Robot):
    """Class for bins of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

        # Unique booleans for Bin instance
        self.slow_down_counter = 0
        self.is_publishing = True
        self.is_empty = True
        self.is_carried = False
        self.designated_picker = None
        self.designated_carrier = None
        self.master = None
        self.should_face = None
        self.empty_response_msg = empty_response()
        self.bin_latch = rospy.Publisher('latched_to_picker', empty_response, queue_size=1)
        # self.bin_full_latch = rospy.Publisher('latched_to_carrier', full_response, queue_size=1)

        def id_response(data):
            # rospy.loginfo("SDAFDFDSFDSAFDSAFDSAFDSAFDSAFSADFADSFSADF")
            if data.bin_id == self.robot_id:

                self.is_publishing = False
                
                robot = robot_storage.getRobotWithId(data.robot_id)
                if robot.type == "PickerRobot":
                    self.designated_picker = data.robot_id
                elif robot.type == "CarrierRobot":
                    self.designated_carrier = data.robot_id
                # rospy.loginfo(self.robot_id + "    " + data.robot_id)
            # self.is_carried = True

        def mimic_now(data):
            if not self.should_face and data.robot_id == self.designated_picker and not self.master:
                if (data.x - 0.5) <= self.position['x'] <= (data.x + 0.5):
                    if (data.y - 0.5) <= self.position['y'] <= (data.y + 0.5):
                        picker = robot_storage.getRobotWithId(data.robot_id)
                        # rospy.loginfo(data.robot_id)
                        self.latch(picker)
                        self.empty_response_msg.robot_id = data.robot_id
                        self.empty_response_msg.bin_id = self.robot_id


            if not self.should_face and data.robot_id == self.designated_carrier and not self.master:
                if (data.x - 0.5) <= self.position['x'] <= (data.x + 0.5):
                    if (data.y - 0.5) <= self.position['y'] <= (data.y + 0.5):
                        carrier = robot_storage.getRobotWithId(data.robot_id)
                        # rospy.loginfo(data.robot_id)
                        self.latch(carrier)
                        self.empty_response_msg.robot_id = data.robot_id
                        self.empty_response_msg.bin_id = self.robot_id

        # Suscribe to topic to recieve response from pickers.
        rospy.Subscriber("empty_response_topic", empty_response, id_response)
        rospy.Subscriber("statuses", robot_status, mimic_now)
        

    def execute_callback(self):
        """Logic for Bin"""
        # rospy.loginfo(str(self.robot_id) + str(self.should_face) + "GOOD")

        if self.should_face:
            if self.master.rotate_to_angle(self.should_face):
                self.master.add_slave(self)  # Set the bin to mimic
                self.bin_latch.publish(self.empty_response_msg)
                self.should_face = None
        if self.is_publishing:  # This boolean is initally True
            rospy.loginfo("BIN: " + self.robot_id + "at " + str(self.position["x"]) + ", " + str(self.position["y"]))
            # Publish message bin's details to let pickers know that it can be picked up.
            bin_pub = rospy.Publisher('bin_status_topic', bin_status, queue_size=1)

            msg = bin_status()
            msg.bin_id = self.robot_id

            if self.master is None:
                msg.is_carried = False
            else:
                msg.is_carried = True

            if self.is_empty:
                msg.is_empty = True
            else:
                msg.is_empty = False

            msg.x = self.position["x"]
            msg.y = self.position["y"]
            rospy.loginfo(msg)
            bin_pub.publish(msg)

    def latch(self, robot):
        self.is_carried = True
        self.master = robot
        robot.stop()
        self.should_face = self.position['theta']
        rospy.loginfo('SHOULD FACE' + str(self.should_face))

    def unlatch(self):
        self.is_carried = False
        self.is_publishing = True
        self.designated_picker = None
        self.designated_carrier = None
        rospy.loginfo('Bin ' + self.robot_id + 'is being unlatched from ' + self.master.robot_id)
        self.master.slave = None
        self.master = None
        self.stop()
