from action import Action
import math
import rospy


class UnlatchAction(Action):
    """
    Drop bin
    """

    def __init__(self, bin):
        self.bin = bin
        self.has_started = False

    def start(self, robot):
        self.has_started = True
        self.bin.stop()
        robot.stop()
        self.bin.unlatch()

    def during(self, robot):
        if not self.has_started:
            self.start(robot)

    def is_finished(self, robot):
        rospy.loginfo('unlatched? ' + str(bool(robot.slave is None and self.bin.master is None)))
        return bool(robot.slave is None and self.bin.master is None)

    def finish(self, robot):
        robot.stop()
        if robot.has_bin:
            robot.has_bin = False
        self.bin.is_publishing = True

    def to_string(self):
        return "Move forward " + str(self.distance)
