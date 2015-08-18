from robot import Robot
import rospy

class Person(Robot):
    """Class for people of simulation"""
    def __init__(self, robot_id, robot_type, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, robot_type, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.direction = "east"

    def execute_callback(self):
        """Movement logic for person"""

        if not self.rotation_executing:
            # # Blocking logic
            # if self.is_blocked():
            #     self.stop()
            #     return
            # self.forward()

            # position = self.get_position()
            # rospy.loginfo(str(position['y']))

            if self.is_blocked() and self.direction is "east": 
                self.rotate_to_west()
                self.direction = "west"
            elif self.is_blocked() and self.direction is "west":
                self.rotate_to_east()
                self.direction = "east"
            # elif (position['y'] > 25) and self.direction is "east":
            #     self.rotate_to_west()
            #     self.direction = "west"
            # elif (position['y'] < 5) and self.direction is "west":
            #     self.rotate_to_east()
            #     self.direction = "east"
            self.forward()
        
        else: 
           if self.direction == "east":
               self.rotate_to_east()
           else:
               self.rotate_to_west()