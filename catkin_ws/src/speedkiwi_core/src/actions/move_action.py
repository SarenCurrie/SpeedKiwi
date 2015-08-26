from action import Action
import math
import rospy


class MoveAction(Action):
    """
    Action to move forward a certain distance in meters
    """

    def __init__(self, d):
        # Initialize variables
        self.distance = d
        self.x_start = 0
        self.y_start = 0

    def start(self, robot):
        # Get current x, y coordinates.
        self.x_start = robot.get_position()['x']
        self.y_start = robot.get_position()['y']
        rospy.loginfo("forward " + str(self.distance) + " - " + str(robot.robot_id))

    def during(self, robot):
        # If blocked, stop, otherwise keep moving forward.
        if robot.is_blocked():
            robot.stop()
        else:
            robot.forward()

    def is_finished(self, robot):
        # If the robot has travelled more than the required distance, the robot is finished.
        delta_x = robot.get_position()['x'] - self.x_start
        delta_y = robot.get_position()['y'] - self.y_start
        delta = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if delta > self.distance:
            return True
        else:
            return False

    def finish(self, robot):
        # Stop when finished.
        robot.stop()

    def to_string(self):
        """String representation of MoveAction"""
        return "Move forward " + str(self.distance)
