from action import Action
import math
import rospy
import random


class MoveRandomAction(Action):
    """
    Random movement action for Animal
    """

    def __init__(self, d):
        self.duration = d
        self.counter = 0

    def start(self, robot):
        rospy.loginfo("Moving randomly" + " - " + str(robot.robot_id))

    def during(self, robot):
        """Behaviour: robot moves forward and rotates randomly, and rotates when it detects collision"""
        self.counter += 1
        randint = random.randint(1, 5)

        if 1 <= randint <= 4 and not robot.is_blocked():
            robot.forward()
        else:
            robot.start_rotate()

    def is_finished(self, robot):
        if self.counter > self.duration:
            return True
        else:
            return False

    def finish(self, robot):
        robot.stop()
