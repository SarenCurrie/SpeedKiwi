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

    def start(self, robot):
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']
        self.x_correct = False
        self.y_correct = False

    def during(self, robot):
        current_x = robot.get_position()['x']
        current_y = robot.get_position()['y']

        self.x_correct = current_x < (self.x + 0.5) and current_x > (self.x - 0.5)
        self.y_correct = current_y < (self.y + 0.5) and current_y > (self.y - 0.5)

        if robot.is_blocked():
            robot.stop()
            direction = robot.get_position()['theta']
            if direction > -math.pi/4 and direction < math.pi/4:
                # North
                pass
            elif direction > -3 * math.pi/4 and direction < -math.pi/4:
                # East
                pass
            elif direction > math.pi/4 and direction < 3 * math.pi/4:
                # West
                pass
            else:
                # South
                pass
        else:
            robot.forward()

    def is_finished(self, robot):
        if self.x_correct and self.y_correct:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()
