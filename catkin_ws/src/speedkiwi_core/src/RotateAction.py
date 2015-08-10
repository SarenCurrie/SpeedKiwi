from Action import Action
import math
import rospy

class RotateAction(Action):
    """
    Action to rotate to face a particular direction
    """
    
    is_rotating = True
    
    def __init__(self, rotation, angle=None):
        self.current_rotation = rotation
        self.target_angle = angle

    def start(self, robot):
        self.is_rotating = True
        if self.current_rotation == "rotate_to_angle":
            rospy.loginfo(self.current_rotation + " " + str(self.target_angle))
        else:
            rospy.loginfo(self.current_rotation)

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
