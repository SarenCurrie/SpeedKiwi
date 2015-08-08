from Action import Action
import math

class MoveAction(Action):
    """
    Example Action
    """
    
    x_start = 0
    y_start = 0
    
    def __init__(self, d):
        self.distance = d

    def start(self, robot):
        """
        robot: The robot that is performing the action.

        Called when the action starts executing.
        This should be overridden if you want behaviour at the start of the action.
        """
        robot.forward()
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']

    def during(self, robot):
        """
        robot: The robot that is performing the action.

        Called during the robot's execute loop.
        This should be overridden to define the Action's behaviour.
        """
        pass

    def is_finished(self, robot):
        """
        robot: The robot that is performing the action.

        Must return true when the action is complete.
        This MUST be overridden or the Action will NEVER finish executing.
        """
        delta = math.sqrt((robot.get_position()['x'] - self.x_start) ** 2 + (robot.get_position()['y'] - self.y_start) ** 2)
        if delta > self.distance:
            return True
        else:
            return False

    def finish(self, robot):
        """
        robot: The robot that is performing the action.

        Called when the command finishes executing.
        This should be overridden if you want behaviour at the end of the action.
        """
        robot.stop()
