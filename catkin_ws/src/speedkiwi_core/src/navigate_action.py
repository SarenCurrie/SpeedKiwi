from action import Action
import math
import rospy

class NavigateAction(Action):
    """
    Example Action
    """

    def __init__(self, x, y):
        self.x_target = x
        self.y_target = y
        self.x_start = 0
        self.y_start = 0
        self.x_correct = False
        self.y_correct = False
        self.current_rotation = None

    def start(self, robot):
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']

    def during(self, robot):
        current_x = robot.get_position()['x']
        current_y = robot.get_position()['y']

        x_diff = current_x - self.x_target
        y_diff = current_y - self.y_target

        self.x_correct = x_diff < 0.5 and x_diff > -0.5
        self.y_correct = y_diff < 0.5 and y_diff > -0.5

        rot_finished = False

        rospy.loginfo(self.current_rotation)

        if not robot.rotation_executing:
            if robot.is_blocked():
                robot.stop()
                direction = robot.get_position()['theta']
                if direction > -math.pi/4 and direction < math.pi/4:
                    robot.rotate_to_north()
                    self.current_rotation = "rotate_to_north"
                elif direction > -3 * math.pi/4 and direction < -math.pi/4:
                    robot.rotate_to_east()
                    self.current_rotation = "rotate_to_east"
                elif direction > math.pi/4 and direction < 3 * math.pi/4:
                    robot.rotate_to_west()
                    self.current_rotation = "rotate_to_west"
                else:
                    robot.rotate_to_south()
                    self.current_rotation = "rotate_to_south"
            else:
                robot.forward()
        else:
            if self.current_rotation == "rotate_to_west":
                rot_finished = robot.rotate_to_west()
            elif self.current_rotation == "rotate_to_east":
                rot_finished = robot.rotate_to_east()
            elif self.current_rotation == "rotate_to_north":
                rot_finished = robot.rotate_to_north()
            elif self.current_rotation == "rotate_to_south":
                rot_finished = robot.rotate_to_south()

        if rot_finished:
            robot.stop()

    def is_finished(self, robot):
        if self.x_correct and self.y_correct:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()
