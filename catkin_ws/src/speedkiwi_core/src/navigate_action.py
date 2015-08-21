from action import Action
import math
import rospy

class NavigateAction(Action):
    """
    Example Action
    """

    ROTATE_COUNTER_THRESHOLD = 100

    def __init__(self, x, y):
        self.x_target = x
        self.y_target = y
        self.x_start = 0
        self.y_start = 0
        self.x_correct = False
        self.y_correct = False
        self.current_rotation = None
        self.rotate_counter = 0
        self.angle = None

    def start(self, robot):
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']
        self.check_direction(robot)

    def during(self, robot):
        if robot.is_blocked():
            self.angle = None
            self.rotate_counter = 0
            robot.start_rotate()
        else:
            robot.stop_rotate()
            if self.rotate_counter > self.ROTATE_COUNTER_THRESHOLD:
                self.check_direction(robot)
            if self.angle:
                if robot.rotate_to_angle(self.angle):
                    self.angle = None
            else:
                robot.forward()
                self.rotate_counter += 1

        current_x = robot.get_position()['x']
        current_y = robot.get_position()['y']

        x_diff = self.x_target - current_x
        y_diff = self.y_target - current_y

        self.x_correct = (abs(x_diff) < 0.5)
        self.y_correct = (abs(y_diff) < 0.5)

    def is_finished(self, robot):
        if self.x_correct and self.y_correct:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()

    def to_string(self):
        return "Navigating to position x:" + str(self.x_target) + " y:" + str(self.y_target)

    def check_direction(self, robot):
        self.rotate_counter = 0

        current_x = robot.get_position()['x']
        current_y = robot.get_position()['y']

        x_diff = self.x_target - current_x
        y_diff = self.y_target - current_y

        self.angle = math.atan2(y_diff, x_diff)
        rospy.loginfo("Checking direction")
