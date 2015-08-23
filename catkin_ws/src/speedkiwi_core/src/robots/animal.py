from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import math
import rospy
from robots import Robot
from actions import MoveAction, RotateAction, NavigateAction
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status
import random


class Animal(Robot):
    """Subclass of Robot which implements random movement"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__
        self.robot_dict = dict()
        self.currently_targeting = False
        self.dict_index = -1
        self.counter = 0
        self.retreat = False

        def robot_locations(data):
            if data.robot_type == "PickerRobot" or data.robot_type == "CarrierRobot":
                self.robot_dict[data.robot_id] = data

        rospy.Subscriber("statuses", robot_status, robot_locations)

    # def execute_callback(self):
    #     """Movement logic for person"""
    #     if self.counter % 100 == 0 and self.robot_dict:
    #         if self._action_queue:
    #             self._action_queue[0].finish(self)
    #             self._action_queue.pop()

    #         self.dict_index = 0

    #         if (self.dict_index >= 0): #need this to check if index is not out of bounds
    #             target_x = self.robot_dict.values()[self.dict_index].x
    #             target_y = self.robot_dict.values()[self.dict_index].y

    #             self.add_action(NavigateAction(target_x, target_y))
    #             rospy.loginfo("Goal " + str(target_x) + "," + str(target_y))

    #     self.counter += 1

    def execute_callback(self):
        """Logic for the animal"""
        if self.retreat:
            current_x = self.position['x']
            current_y = self.position['y']
            target_x = self.x_offset
            target_y = self.y_offset
            distance = math.sqrt((float(current_x)-float(target_x))**2 + (float(current_y)-float(target_y))**2)
            if distance >= 1:
                rospy.loginfo("Dog has arrived in the kennel")
                return
            else:
                self.retreat = False
        # rospy.loginfo("dict size: " + str(len(self.robot_dict)) + " index: " + str(self.dict_index) + " targeting: " + str(self.currently_targeting))
        if (self.currently_targeting is False and bool(self.robot_dict)):
            self.dict_index = random.randint(0, len(self.robot_dict) - 1)
            self.currently_targeting = True
            return

        if (self.dict_index >= 0 and self.counter >= 100):
            self.acquire_target()  # get new target coordinates every 100 cycles
            self.counter = 0
        self.counter += 1

        if (self.dict_index >= 0 and self.get_distance_from_target() <= 4):
            if bool(self._action_queue):
                rospy.loginfo("The dog goes bark")
                self._action_queue[0].finish(self)
                self._action_queue.pop()
            self.add_action(NavigateAction(self.x_offset, self.y_offset))
            rospy.loginfo("Dog navigating back to kennel")
            self.retreat = True
            self.currently_targeting = False

    def acquire_target(self):
        target_x = self.robot_dict.values()[self.dict_index].x
        target_y = self.robot_dict.values()[self.dict_index].y
        target_id = self.robot_dict.values()[self.dict_index].robot_id
        rospy.loginfo(self.robot_id + " targeting " + str(target_id) + " at " + str(target_x) + "," + str(target_y))
        if bool(self._action_queue):
            rospy.loginfo("execute bool thing")
            self._action_queue[0].finish(self)
            self._action_queue.pop()
        self.add_action(NavigateAction(target_x, target_y))

    def get_distance_from_target(self):
        current_x = self.position['x']
        current_y = self.position['y']
        target_x = self.robot_dict.values()[self.dict_index].x
        target_y = self.robot_dict.values()[self.dict_index].y
        distance = math.sqrt((float(current_x)-float(target_x))**2 + (float(current_y)-float(target_y))**2)
        return distance
