from robots import Robot
import rospy
import os
from speedkiwi_msgs.msg import bin_status, empty_response, full_response, robot_status
from actions import NavigateAction, UnlatchAction
from world_locations import bin_locations
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
        self.has_bin = False
        self.counter = 0
        self.going_towards = None

        empty_response_pub = rospy.Publisher('empty_response_topic', empty_response, queue_size=10)

        def callback(data):
            if not data.is_empty:
                self.current_bin_x = data.x
                self.current_bin_y = data.y

                if self.is_closest() and not self.has_bin:  # and not self.slave and not data.is_carried:
                    current_bin = robot_storage.getRobotWithId(data.bin_id)
                    if current_bin.designated_carrier == None:
                        rospy.loginfo("Carrier bot coming towards bin " + data.bin_id + " at " + str(self.current_bin_x) + ", " + str(self.current_bin_y))

                        self.has_bin = True
                        self.add_action(NavigateAction(self.current_bin_x, self.current_bin_y))
                        rospy.loginfo("P Robot: " + self.robot_id + "    " + "Bin closest: " + data.bin_id)
                        msg = empty_response()
                        msg.robot_id = self.robot_id
                        msg.bin_id = data.bin_id

                        empty_response_pub.publish(msg)
                        self.going_towards = data.bin_id

        def bin_carrying(data):
            if data.robot_id == self.robot_id:
                rospy.loginfo("carrier " + self.robot_id + " going up to driveway")
                carrierx = robot_storage.getRobotWithId(data.robot_id)
                for i in range(0,3):
                    if not bin_locations[i]['occupied']:
                        bin_locations[i]['occupied'] = True
                        self.add_action(NavigateAction(bin_locations[i]['x'], bin_locations[i]['y']))
                        self.add_action(UnlatchAction(self.slave))
                        break
                    if i is 3:
                        # Locations should never be all full, but who knows?
                        bin_locations[i]['occupied'] = True
                        self.add_action(NavigateAction(bin_locations[i]['x'], bin_locations[i]['y']))

        rospy.Subscriber("latched_to_picker", empty_response, bin_carrying)        

        rospy.Subscriber("bin_status_topic", bin_status, callback)

    def execute_callback(self):
        """Logic for the carrier robot."""
        currentX = self.position['x']
        currentY = self.position['y']

        self.current_speed = self.top_speed

    def is_closest(self):
        """Check if this carrier is the closest to the specified bin."""

        def dist(x, y):
            d = math.sqrt((float(x)-float(self.current_bin_x))**2 + (float(y)-float(self.current_bin_y))**2)
            # rospy.loginfo("Returning distance: %d", d)
            return d

        robot_list = robot_storage.get_robot_list()

        for p in robot_list:
            if robot_list[p].type == "CarrierRobot" and not robot_list[p].has_bin:
                if not robot_list[p].robot_id == self.robot_id:
                    if dist(self.position['x'], self.position['y']) > dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        # rospy.loginfo(robot_list[p].robot_id + "Wasn't the closest to %.1f" % self.current_bin_x)
                        return False
                    elif dist(self.position['x'], self.position['y']) == dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        if int(self.robot_id[6:]) > int(robot_list[p].robot_id[6:]):
                            # rospy.loginfo("I wasn't the closest =")
                            return False

        # rospy.loginfo(self.robot_id + "was the closest! %.1f" % self.current_bin_x)
        return True

