from robots import Robot
from std_msgs.msg import String
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status
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


        self.master = None

        def id_response(data):
            # If bin recieves own id back, stop publishing.
            #rospy.loginfo("Data: %s - Self: %s", data.bin_id, self.robot_id)

            if data.bin_id == self.robot_id:
                self.is_publishing = False
                self.designated_picker = data.picker_id
                #rospy.loginfo(str(self.is_publishing))
            #self.is_carried = True

        def mimic_now(data):
            rospy.loginfo(self.robot_id)
            if data.robot_id == self.designated_picker:
                rospy.loginfo("?????")
                if int(data.x) == int(self.position['x']):
                    rospy.loginfo("DID_IT_WORK?????")
                    if int(data.y) == int(self.position['y']):
                        rospy.loginfo("DID_IT_WORK?????")

                        picker = robot_storage.getRobotWithId(data.robot_id)
                        rospy.loginfo(data.robot_id)
                        self.latch(picker)
                        bin_latch = rospy.Publisher('latched_to_picker', empty_response, queue_size=10)
                        msg = empty_response()
                        msg.picker_id = data.robot_id
                        msg.bin_id = self.robot_id
                        bin_latch.publish(msg)


        # Suscribe to topic to recieve response from pickers.
        rospy.Subscriber("empty_response_topic", empty_response, id_response)

        rospy.Subscriber("statuses", robot_status, mimic_now)


    def execute_callback(self):
        """Logic for Bin"""
        if self.slow_down_counter < 10:
            self.slow_down_counter += 1
        else:
            if self.is_publishing: # This boolean is initally True

                # Publish message bin's details to let pickers know that it can be picked up.
                bin_pub = rospy.Publisher('bin_status_topic', bin_status, queue_size=10)

                msg = bin_status()
                msg.bin_id = self.robot_id

                if self.master == None:
                    msg.is_carried = False
                else:
                    msg.is_carried = True 

                msg.x = self.position["x"]
                msg.y = self.position["y"]
                bin_pub.publish(msg)

    def latch(self, robot):
        self.master = robot
        robot.add_slave(self)



