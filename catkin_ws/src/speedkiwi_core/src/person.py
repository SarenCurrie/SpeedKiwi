from robot import Robot
import rospy

class Person(Robot):
    """Class for people of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.direction = "north"

    def execute_callback(self):
        """Movement logic for person"""

        if not self.rotation_executing:
            # Blocking logic
            if self.is_blocked():
                self.stop()
                return

            self.forward()

            position = self.get_position()
            rospy.loginfo(str(position['y']))

            if (position['y'] > 10) and self.direction is "north": 
                self.rotate_to_south()
                self.direction = "south"
            elif (position['y'] < 0) and self.direction is "south":
                self.rotate_to_north()
                self.direction = "north"
            self.forward()
        
        else: 
           if self.direction == "north":
               self.rotate_to_north()
           else:
               self.rotate_to_south()