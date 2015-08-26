from action import Action
from move_action import MoveAction
from rotate_action import RotateAction
import math
import rospy


class Figure8Action(Action):
    """
    This action is intended to be used for testing rotation methods.

    This action makes the robot move in a figure of eight shape. This requires the robot uses all four rotate_to_XXXX methods (e.g. rotate_to_north) in both directions (clockwise/anticlockwise).

    This action works by adding a set of rotate and move actions to the action queue. It then adds another figure 8 action to the queue effectively causing the robot to perform figure 8's.
    """

    def __init__(self):
        # Initialize variable
        self.is_rotating = True

    def start(self, robot):
        # rospy.loginfo("Figure 8 Action" + " - " + str(robot.robot_id))
        robot.add_action(RotateAction("rotate_to_east"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_north"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_west"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_north"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_east"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_south"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_west"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_south"))
        robot.add_action(MoveAction(5))
        robot.add_action(Figure8Action())

    def during(self, robot):
        robot.add_action(RotateAction("rotate_to_east"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_north"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_west"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_north"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_east"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_south"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_west"))
        robot.add_action(MoveAction(5))
        robot.add_action(RotateAction("rotate_to_south"))
        robot.add_action(MoveAction(5))
        robot.add_action(Figure8Action())
        self.is_rotating = False

    def is_finished(self, robot):
        # Is finished if not rotating.
        return not self.is_rotating

    def finish(self, robot):
        # Stop if finished.
        robot.stop()

    def to_string(self):
        # String representation of Figure 8 Action.
        return "Figure of eight"
