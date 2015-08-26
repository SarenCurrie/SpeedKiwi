from action import Action
import math
import rospy


class RotateAction(Action):
    """
    Action to rotate to face a particular direction
    """

    def __init__(self, rotation, angle=None):
        """ Initialize variables """
        self.is_rotating = False
        self.current_rotation = rotation
        self.target_angle = angle

    def start(self, robot):
        """ Start rotation """
        self.is_rotating = True
        rospy.loginfo(str(robot.robot_id) + ": " + self.to_string())

    def during(self, robot):
        """ Use one of the rotation methods depending on the rotation selected. """
        finished = False
        if self.current_rotation == "rotate_to_west":
            finished = robot.rotate_to_west()
        elif self.current_rotation == "rotate_to_east":
            finished = robot.rotate_to_east()
        elif self.current_rotation == "rotate_to_north":
            finished = robot.rotate_to_north()
        elif self.current_rotation == "rotate_to_south":
            finished = robot.rotate_to_south()
        elif self.current_rotation == "rotate_to_angle":
            finished = robot.rotate_to_angle(self.target_angle)
        if finished:
            self.is_rotating = False

    def is_finished(self, robot):
        """ Is finished if not rotating. """
        return not self.is_rotating

    def finish(self, robot):
        """ Stop when finished. """
        robot.stop()

    def to_string(self):
        """ String representation of RotateAction. """
        if self.current_rotation == "rotate_to_angle":
            return "rotating to angle " + str(self.target_angle)
        else:
            return str(self.current_rotation)
