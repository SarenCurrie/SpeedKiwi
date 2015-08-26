from robot import Robot


class DifferentRobot(Robot):
    """Robot used for testing during the earlier phases of the project."""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        self.type = type(self).__name__

    def execute_callback(self):
        """Movement logic for DifferentRobot."""
        if not (self.curr_robot_messages[3] == None):
            if self.curr_robot_messages[3].is_blocked:
                self.start_rotate()
            else:
                self.stop_rotate()
