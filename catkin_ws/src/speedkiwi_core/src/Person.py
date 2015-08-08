from Robot import Robot

class Person(Robot):
    """Class for people of simulation"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)

    def execute_callback(self):
        """Movement logic for person"""
        position = self.get_position()
        if position['x'] > 10 or position['y'] > 10:
            self.set_velocity(-self.top_speed)
        elif position['x'] < -10 or position['y'] < -10:
            self.set_velocity(self.top_speed)