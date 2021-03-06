from robots import Robot
import rospy
import os
from speedkiwi_msgs.msg import bin_status, empty_response, robot_status, full_response
from actions import NavigateAction, NavigatePickAction, UnlatchAction
from world_locations import locations
import robot_storage
import random
from std_msgs.msg import String
import math


class PickerRobot(Robot):

    MAX_FRUIT = 5
    PICK_SPEED = 1

    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)

        #define max/min coordinates for orchard space
        boundaries = locations.get_orchard_boundaries()
        self.maxX = boundaries["max_x"]
        self.maxY = boundaries["max_y"]
        self.minX = boundaries["min_x"]
        self.minY = boundaries["min_y"]
        self.has_bin = False
        self.type = type(self).__name__

        # Unique variables for picker robots
        # self.picker_dict = dict()
        self.current_bin_x = 0
        self.current_bin_y = 0

        self.fruit_count = 0

        self.has_finished = False

        empty_response_pub = rospy.Publisher('empty_response_topic', empty_response, queue_size=10)

        def callback(data):
            """Execute method in response to "bin_status" message."""
            if data.is_empty:
                # Data used to calculate if it's the closest to the bin
                rospy.loginfo("Bin call: " + data.bin_id + " %.1f       %.1f" % (data.x, data.y))
                self.current_bin_x = data.x
                self.current_bin_y = data.y
            
                # rospy.loginfo(len(self.picker_dict))
                if self.is_closest() and not self.has_bin:  # and not self.slave and not data.is_carried:
                    self.has_finished = False
                    current_bin = robot_storage.getRobotWithId(data.bin_id)
                    if current_bin.designated_picker == None:
                        self.has_bin = True
                        self.add_action(NavigateAction(self.current_bin_x, self.current_bin_y))
                        rospy.loginfo("P Robot: " + self.robot_id + "    " + "Bin closest: " + data.bin_id)
                        msg = empty_response()
                        msg.robot_id = self.robot_id
                        msg.bin_id = data.bin_id
                        rospy.loginfo(self.robot_id + msg.robot_id + msg.bin_id + data.bin_id)
                        empty_response_pub.publish(msg)
                        rospy.loginfo("??????????????????////???????????????????")

        def initiate_picking(data):
            if data.robot_id == self.robot_id:
                pickerx = robot_storage.getRobotWithId(data.robot_id)
                self.x_start = self.position['x']
                self.y_start = self.position['y']
                self.add_action(NavigatePickAction(pickerx.position["x"], self.maxY + 5))

        rospy.Subscriber("bin_status_topic", bin_status, callback)

        # rospy.Subscriber("statuses", robot_status, picker_locations)

        rospy.Subscriber("latched_to_picker", empty_response, initiate_picking)

    def execute_callback(self):
        """Logic for the picker robot."""
        currentX = self.position['x']
        currentY = self.position['y']
        inOrchard = False  # used for debugging purposes
        # check if in orchard area
        if ((self.minX <= currentX <= self.maxX) and (self.minY <= currentY <= self.maxY)):
            inOrchard = True
            self.do_picking()
            self.current_speed = self.PICK_SPEED  # slow down to picking speed
        else:
            self.current_speed = self.top_speed

        #if self.current_bin_x == self.position['x'] and self.current_bin_y == self.position['y']:
        #    empty_response_pub = rospy.Publisher('empty_response_topic', String, queue_size=1)

        #    empty_response_pub.publish("Latch")

    def do_picking(self):
        """Execute picking behaviour"""
        # rospy.loginfo(self.robot_id + " is picking!")
        if self.check_full() == True:
            if not self.has_finished:
                self.finish_picking()
            return

        self.randint = random.randint(1, 10)
        if self.randint == 1:
            self.fruit_count += 1
            rospy.loginfo(self.robot_id + " has picked " + str(self.fruit_count) + " kiwifruit!")
            if self.check_full():
                rospy.loginfo(self.robot_id + " is full")

    def finish_picking(self):
        self.has_finished = True
        self.slave.is_empty = False
        self.add_action(NavigateAction(self.minX - 5, self.maxY + 5))
        self.add_action(NavigateAction(self.minX - 5, self.minY - 5))
        self.add_action(NavigateAction(self.x_start, self.y_start))  # Go to bin's starting position
        self.add_action(UnlatchAction(self.slave))  # Drop bin
        self.add_action(NavigateAction(self.x_offset, self.y_offset))  # Return to starting position

    def is_closest(self):
        """Check if this picker is the closest to the specified bin."""

        def dist(x, y):
            """Calculate distance from this robot to the current bin."""
            d = math.sqrt((float(x)-float(self.current_bin_x))**2 + (float(y)-float(self.current_bin_y))**2)
            # rospy.loginfo("Returning distance: %d", d)
            return d

        robot_list = robot_storage.get_robot_list()

        for p in robot_list:
            if robot_list[p].type == "PickerRobot" and not robot_list[p].has_bin:
                if not robot_list[p].robot_id == self.robot_id:
                    # rospy.loginfo("I'm picker robot: " + robot_list[p].robot_id + "My Distance from bin %.1f is: %.1f" % (self.current_bin_x, dist(robot_list[p].position['x'], robot_list[p].position['y']))) # hi picker robot: " + robot_list[p].robot_id, I'm Dad!

                    if dist(self.position['x'], self.position['y']) > dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        # rospy.loginfo(robot_list[p].robot_id + "Wasn't the closest to %.1f" % self.current_bin_x)
                        return False
                    elif dist(self.position['x'], self.position['y']) == dist(robot_list[p].position['x'], robot_list[p].position['y']):
                        if int(self.robot_id[6:]) > int(robot_list[p].robot_id[6:]):
                            # rospy.loginfo("I wasn't the closest =")
                            return False

        # rospy.loginfo(self.robot_id + "was the closest! %.1f" % self.current_bin_x)
        return True

    def check_full(self):
        """Check if bin should be full."""
        if self.fruit_count >= self.MAX_FRUIT:
            return True
        return False

    def empty_bin(self):
        """Reset fruit count to zero."""
        self.fruit_count = 0
