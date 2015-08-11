from action import Action
import math

class NavigateAction(Action):
    """
    Example Action
    """
    
    x_start = 0
    y_start = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
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

        self.x_correct = current_x < (self.x + 0.5) and current_x > (self.x - 0.5)
        self.y_correct = current_y < (self.y + 0.5) and current_y > (self.y - 0.5)

        if not robot.rotation_executing:
            if robot.is_blocked():
                robot.stop()
                direction = robot.get_position()['theta']
                # if direction > -math.pi/4 and direction < math.pi/4:
                #     robot.rotate_to_east()
                #     self.current_rotation = "rotate_to_east"
                #     pass
                # elif direction > -3 * math.pi/4 and direction < -math.pi/4:
                #     robot.rotate_to_south()
                #     self.current_rotation = "rotate_to_south"
                #     pass
                # elif direction > math.pi/4 and direction < 3 * math.pi/4:
                #     robot.rotate_to_north()
                #     self.current_rotation = "rotate_to_north"
                #     pass
                # else:
                robot.rotate_to_west()
                self.current_rotation = "rotate_to_west"
                pass
            else:
                robot.forward()
        else:
            if self.current_rotation == "rotate_to_west":
                finished = robot.rotate_to_west()
            elif self.current_rotation == "rotate_to_east":
                finished = robot.rotate_to_east()
            elif self.current_rotation == "rotate_to_north":
                finished = robot.rotate_to_north()
            elif self.current_rotation == "rotate_to_south":
                finished = robot.rotate_to_south()

    def is_finished(self, robot):
        if self.x_correct and self.y_correct:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()
