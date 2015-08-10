from Action import Action
import math

class NavigateAction(Action):
    """
    Example Action
    """
    
    x_start = 0
    y_start = 0
    
    def __init__(self, d):
        self.distance = d

    def start(self, robot):
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']

    def during(self, robot):
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
        delta = math.sqrt((robot.get_position()['x'] - self.x_start) ** 2 + (robot.get_position()['y'] - self.y_start) ** 2)
        if delta > self.distance:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()
