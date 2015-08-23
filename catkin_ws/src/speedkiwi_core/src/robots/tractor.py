from robots import Robot
from actions import NavigateAction, MoveAction, RotateAction
import rospy
import os


class Tractor(Robot):
    """Class for tractor in simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)

        path = os.path.dirname(__file__)
        path = os.path.join(path, "../world_locations/")
        with open(path + "world_perimeter.txt", 'r') as file:
            data = file.readlines()
        self.min_x = int(data[2])
        self.max_x = int(data[4])
        self.min_y = int(data[6])
        self.max_y = int(data[8])

        file.close()

        self.was_blocked = False
        self.old_queue = []

        self.d = 5.5

    def execute_callback(self):
        """Movement logic for a tractor"""
        if self.is_blocked():
            if not self.was_blocked:
                self.was_blocked = True
                rospy.loginfo(str(self._action_queue[0].to_string()))
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
