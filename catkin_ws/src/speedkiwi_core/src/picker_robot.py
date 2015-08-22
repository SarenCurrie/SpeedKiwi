from robot import Robot
import rospy
import os
from speedkiwi_core.msg import empty_response

class PickerRobot(Robot):

    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        #Define orchard edge coordinates
        dir = os.path.dirname(__file__)
        path = os.path.join(dir,"world_locations/")
        with open(path + "orchard.txt", 'r') as file:
            #read orchard location file
            data = file.readlines()

        self.maxX = float(data[1]) 
        self.maxY = float(data[2])
        self.minX = float(data[3])
        self.minY = float(data[4])
        file.close()
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
<<<<<<< HEAD
        """docstring for execute_callback"""
        currentX = self.position['x']
        currentY = self.position['y']
        inOrchard = False #used for debugging purposes
        #check if in orchard area
        if ((self.minX <= currentX <= self.maxX) and (self.minY <= currentY <= self.maxY)):
            inOrchard = True
            self.do_picking()
            """need to slow down robot to 0.01m/s"""

    def do_picking(self):
        """Execute picking behaviour"""
        rospy.loginfo(self.robot_id + " is picking!")
=======
        """Logic for the picker robot."""

    def is_closest(self):
        """Check if this picker is the closest to the specified bin."""
        return 1
>>>>>>> master
