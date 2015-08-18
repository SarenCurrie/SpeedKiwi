from action import Action
import math
import rospy


class RotateAction(Action):
    """
    Action to rotate to face a particular direction
    """
    is_rotating = True
    
    def __init__(self, rotation, angle=None):
        self.is_rotating = False
        self.current_rotation = rotation
        self.target_angle = angle

    def start(self, robot):
        self.is_rotating = True
        rospy.loginfo(self.to_string() + " - " + str(robot.robot_id))

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
        elif self.current_rotation == "rotate_to_angle":
            finished = robot.rotate_to_angle(self.target_angle)
        if finished:
            self.is_rotating = False

    def is_finished(self, robot):
        return not self.is_rotating

    def finish(self, robot):
        robot.stop()

    def to_string(self):
        if self.current_rotation == "rotate_to_angle":
            return self.current_rotation + " " + str(self.target_angle)
        else:
            return str(self.current_rotation)