from robots import Robot
from actions import NavigateAction
from world_locations import locations
import rospy
import random
import os
import sys


class Person(Robot):
    """Class for people of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.counter = 0

        boundaries = locations.get_wall_boundaries()
        self.min_x = int(boundaries["min_x"])
        self.max_x = int(boundaries["max_x"])
        self.min_y = int(boundaries["min_y"])
        self.max_y = int(boundaries["max_y"])

    def execute_callback(self):
        """Movement logic for person"""
        # Safety check for counter value
        if self.counter == sys.maxint:
            self.counter = 0

        # Every 100 execution loops, generate random set of coordinates.
        if self.counter % 100 == 0:
            # rospy.loginfo("Counter:" + str(self.counter))

            if self._action_queue:
                self._action_queue[0].finish(self)
                self._action_queue.pop()

            x_target = random.randint(self.min_x, self.max_x)
            y_target = random.randint(self.min_y, self.max_y)

            # Navigate to new random set of coordinates
            self.add_action(NavigateAction(x_target, y_target))
            # rospy.loginfo("Uneducate person is going towards: " + str(x_target) + ", " + str(y_target))

        self.counter += 1
