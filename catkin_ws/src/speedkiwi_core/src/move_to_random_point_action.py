from action import Action
import math
import rospy
import random
import os

class MoveToRandomPointAction(Action):
    """
    Generates a random point to move to every 10 seconds. Used for uneducated person.
    """

    def __init__(self):
        self.duration = 1000
        self.counter = 0

        # Point to go to
        self.goal_x = 0
        self.goal_y = 0

        # Boundaries
        path = os.path.dirname(__file__) 
        path = os.path.join(path, "world_locations/")
        with open(path + "world_perimeter.txt", 'r') as file:
            data = file.readlines()
        self.min_x = data[2]
        self.max_x = data[4]
        self.min_y = data[6]
        self.max_y = data[8]

        file.close()
        rospy.loginfo("X Bounds" + str(self.min_x) + "," + str(self.max_x))
        rospy.loginfo("Y Bounds" + str(self.min_y) + "," + str(self.max_y))

    def start(self, robot):
        #self.generate_random_point()
        rospy.loginfo(self.to_string + " - " + str(self.goal_x) + str(self.goal_y) + " - " + str(robot.robot_id))

    def during(self, robot):
        """Behaviour: moves towards randomly generated point, and rotates when it detects collision"""

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

    def to_string(self):
        return "Moving to randomly generated point."

    #def generate_random_point(self):
