from robots import Robot
from actions import NavigateAction, MoveAction, RotateAction
from world_locations import locations
import rospy
import os


class Tractor(Robot):
    """Class for tractor in simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)

        boundaries = locations.get_wall_boundaries()
        self.min_x = boundaries["min_x"]
        self.max_x = boundaries["max_x"]
        self.min_y = boundaries["min_y"]
        self.max_y = boundaries["max_y"]

        self.was_blocked = False
        self.old_queue = []

        self.d = 5.5

    def execute_callback(self):
        """Movement logic for a tractor"""
        if self.is_blocked():
            if not self.was_blocked:
                self.was_blocked = True
                rospy.loginfo("Tractor is: " + str(self._action_queue[0].to_string()))
                self.old_queue = self._action_queue
                self._action_queue = []
                self.stop()
                self.stop_rotate()
        elif self.was_blocked:
            self.was_blocked = False
            self._action_queue = self.old_queue

        elif len(self._action_queue) == 0:
            self.add_action(NavigateAction(self.min_x+self.d, self.min_y+self.d))
            self.add_action(NavigateAction(self.max_x-self.d, self.min_y+self.d))
            self.add_action(NavigateAction(self.max_x-self.d, self.max_y-self.d))
            self.add_action(NavigateAction(self.min_x+self.d, self.max_y-self.d))
