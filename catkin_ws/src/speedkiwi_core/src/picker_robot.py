from robot import Robot


class PickerRobot(Robot):
    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, robot_type, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, robot_type, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)

    def execute_callback(self):
        """docstring for execute_callback"""
        # position = self.get_position()
        # if position['x'] > 20 or position['y'] > 20:
        #     self.set_linear_velocity(-self.top_speed)
        # elif position['x'] < -20 or position['y'] < -20:
        #     self.set_linear_velocity(self.top_speed)
