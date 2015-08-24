from robots import Robot
import rospy
import os
from speedkiwi_msgs.msg import bin_status, full_response, robot_status
from actions import NavigateAction
import robot_storage
import random
from std_msgs.msg import String
import math


class CarrierRobot(Robot):
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

        # Unique variables for carrier robots
        self.carrier_dict = dict()
        self.current_bin_x = 0
        self.current_bin_y = 0
        self.going_towards = None
        self.counter = 0

        def callback(data):
            self.current_bin_x = data.x
            self.current_bin_y = data.y

            if self.is_closest() and not self.slave and not data.is_carried and not data.is_empty and not self.going_towards:
                rospy.loginfo("Carrier bot coming towards bin " + data.bin_id + " at " + str(self.current_bin_x) + ", " + str(self.current_bin_y))
                full_response_pub = rospy.Publisher('full_response_topic', full_response, queue_size=10)
                self.add_action(NavigateAction(self.current_bin_x, self.current_bin_y))

                msg = full_response()
                msg.robot_id = self.robot_id
                msg.bin_id = data.bin_id

                full_response_pub.publish(msg)
                self.going_towards = data.bin_id

        def carrierLocations(data):
            #rospy.loginfo("Data: %s - Self: %s", data.robot_type, "CarrierRobot")
            if data.robot_type == "CarrierRobot":
                if not data.robot_id == self.robot_id:
                    self.carrier_dict[data.robot_id] = data


        rospy.Subscriber("bin_status_topic", bin_status, callback)
        rospy.Subscriber("statuses", robot_status, carrierLocations)

    def execute_callback(self):
        """Logic for the carrier robot."""
        currentX = self.position['x']
        currentY = self.position['y']

        self.current_speed = self.top_speed

        if self.current_bin_x == self.position['x'] and self.current_bin_y == self.position['y']:
            full_response_pub = rospy.Publisher('full_response_topic', String, queue_size=10)

    def is_closest(self):
        """Check if this carrier is the closest to the specified bin."""
        def dist(x, y):
            d = math.sqrt((float(x)-float(self.current_bin_x))**2 + (float(y)-float(self.current_bin_y))**2)
            rospy.loginfo("Returning Distance: %d", d)
            return d

        robot_list = robot_storage.get_robot_list()

        for p in robot_list:
            if robot_list[p].type == "CarrierRobot":
                if not robot_list[p].robot_id == self.robot_id:
                    rospy.loginfo("I'm carrier robot: " + robot_list[p].robot_id + "My Distance from bin %.1f is: %.1f" % (self.current_bin_x, dist(robot_list[p].position['x'], robot_list[p].position['y'])))

                    if dist(self.position['x'], self.position['y']) > dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        rospy.loginfo(robot_list[p].robot_id + "Wasn't the closest to %.1f" % self.current_bin_x)
                        return False
                    elif dist(self.position['x'], self.position['y']) == dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        if int(self.robot_id[6:]) > int(robot_list[p].robot_id[6:]):
                            rospy.loginfo("I wasn't the closest =")
                            return False

        rospy.loginfo(self.robot_id + "was the closest!!!!!!!!!! %.1f" % self.current_bin_x)
        return True

