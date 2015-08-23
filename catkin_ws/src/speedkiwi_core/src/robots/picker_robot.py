from robots import Robot
import rospy
import os
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status
from actions import NavigateAction
import random
from std_msgs.msg import String
import math

class PickerRobot(Robot):

    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        #Define orchard edge coordinates
        dir = os.path.dirname(__file__)
        path = os.path.join(dir,"../world_locations/")
        with open(path + "orchard.txt", 'r') as file:
            #read orchard location file
            data = file.readlines()

        self.maxX = float(data[1]) 
        self.maxY = float(data[2])
        self.minX = float(data[3])
        self.minY = float(data[4])
        file.close()
        self.type = type(self).__name__

        # Unique variables for picker robots
        self.picker_dict = dict()
        self.is_carrying = False
        self.current_bin_x = 0
        self.current_bin_y = 0
        
        self.fruit_count = 0
        self.max_fruit = 100

        def callback(data):
            self.current_bin_x = data.x
            self.current_bin_y = data.y

            if self.is_closest() and not self.is_carrying and not data.is_carried:

                empty_response_pub = rospy.Publisher('empty_response_topic', empty_response, queue_size=10)

                self.add_action(NavigateAction(self.current_bin_x, self.current_bin_y))

                msg = empty_response()
                msg.picker_id = self.robot_id
                msg.bin_id = data.bin_id

                empty_response_pub.publish(msg)
                self.is_carrying = True

        def pickerLocations(data):

            #rospy.loginfo("Data: %s - Self: %s", data.robot_type, "PickerRobot")

            if data.robot_type == "PickerRobot":
                if not data.robot_id == self.robot_id:
                    self.picker_dict[data.robot_id] = data

        rospy.Subscriber("bin_status_topic", bin_status, callback)

        rospy.Subscriber("statuses", robot_status, pickerLocations)

    def execute_callback(self):
        """Logic for the picker robot."""
        currentX = self.position['x']
        currentY = self.position['y']
        inOrchard = False #used for debugging purposes
        #check if in orchard area
        if ((self.minX <= currentX <= self.maxX) and (self.minY <= currentY <= self.maxY)):
            inOrchard = True
            self.do_picking()
            self.current_speed = 0.25 #slow down to picking speed
        else:
            self.current_speed = self.top_speed

    def do_picking(self):
        """Execute picking behaviour"""
        #rospy.loginfo(self.robot_id + " is picking!")
        if self.check_full() == True:
            rospy.loginfo(self.robot_id + " is full")
            return
        
        randint = random.randint(1,10)
        if randint == 1:
            self.fruit_count += 1
            rospy.loginfo(self.robot_id + " has picked " + str(self.fruit_count) + " kiwifruit!")

    def is_closest(self):
        """Check if this picker is the closest to the specified bin."""
        
        def dist(x, y):
            d = math.sqrt( (float(x)-float(self.current_bin_x))**2 + (float(y)-float(self.current_bin_y))**2)
            #rospy.loginfo("Returning distance: %d", d)
            return d
            
        for p in self.picker_dict:
            if dist(self.position['x'], self.position['y']) > dist(self.picker_dict[p].x, self.picker_dict[p].y):
                return False
            elif dist(self.position['x'], self.position['y']) == dist(self.picker_dict[p].x, self.picker_dict[p].y):
                if int(self.robot_id[6:]) > int(self.picker_dict[p].robot_id[6:]):
                    return False

        return True

    def check_full(self):
        if self.fruit_count >= self.max_fruit:
            return True
        return False

    def empty_bin(self):
        self.fruit_count = 0
