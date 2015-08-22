from robots import Robot
from actions import NavigateAction
import rospy
import random
import os

class Person(Robot):
    """Class for people of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.direction = "east"
        self.counter = 0

        path = os.path.dirname(__file__) 
        path = os.path.join(path, "../world_locations/")
        with open(path + "world_perimeter.txt", 'r') as file:
            data = file.readlines()
        self.min_x = int(data[2])
        self.max_x = int(data[4])
        self.min_y = int(data[6])
        self.max_y = int(data[8])

        file.close()

    def execute_callback(self):
        """Movement logic for person"""
        if self.counter % 100 == 0:
            if self._action_queue:
                self._action_queue[0].finish(self)
                self._action_queue.pop()

            x_target = random.randint(self.min_x, self.max_x)
            y_target = random.randint(self.min_y, self.max_y)

            self.add_action(NavigateAction(x_target, y_target))
            rospy.loginfo("Goal " + str(x_target) + "," + str(y_target))

        self.counter += 1

        # goal_x = random.randint(self.min_x, self.max_x)
        # goal_y = random.randint(self.min_x, self.max_y)

        
        
        
        # if not self.rotation_executing:
        #     # # Blocking logic
        #     # if self.is_blocked():
        #     #     self.stop()
        #     #     return
        #     # self.forward()

        #     # position = self.get_position()
        #     # rospy.loginfo(str(position['y']))

        #     if self.is_blocked() and self.direction is "east": 
        #         self.rotate_to_west()
        #         self.direction = "west"
        #     elif self.is_blocked() and self.direction is "west":
        #         self.rotate_to_east()
        #         self.direction = "east"
        #     # elif (position['y'] > 25) and self.direction is "east":
        #     #     self.rotate_to_west()
        #     #     self.direction = "west"
        #     # elif (position['y'] < 5) and self.direction is "west":
        #     #     self.rotate_to_east()
        #     #     self.direction = "east"
        #     self.forward()
        
        # else: 
        #    if self.direction == "east":
        #        self.rotate_to_east()
        #    else:
        #        self.rotate_to_west()