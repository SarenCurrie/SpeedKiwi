from action import Action
from move_action import MoveAction
from rotate_action import RotateAction
import math
import rospy

class Figure8Action(Action):
    """
    Action to drive in a figure of 8 shape repetatively forever
    """
    
    is_rotating = True
    
    def __init__(self):
        self.is_rotating = True

    def start(self, robot):
        rospy.loginfo("Figure 8 Action" + " - " + str(robot.robot_id))
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
        return not self.is_rotating

    def finish(self, robot):
        robot.stop()
