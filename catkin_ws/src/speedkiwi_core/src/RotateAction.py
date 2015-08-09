from Action import Action
import math


class RotateAction(Action):
    """
    Example Action
    """

    def __init__(self, rotation):
        self.is_rotating = False
        self.current_rotation = rotation

    def start(self, robot):
        self.is_rotating = True

    def during(self, robot):
        finished = False
        if self.current_rotation == "rotate_to_west":
            finished = robot.rotate_to_west()
        elif self.current_rotation == "rotate_to_east":
            finished = robot.rotate_to_east()
        elif self.current_rotation == "rotate_to_north":
            finished = robot.rotate_to_north()
        elif self.current_rotation == "rotate_to_south":
            finished = robot.rotate_to_south()
        if finished:
            self.is_rotating = False

    def is_finished(self, robot):
        return not self.is_rotating

    def finish(self, robot):
        robot.stop()
