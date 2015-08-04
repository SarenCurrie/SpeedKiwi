from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
from speedkiwi_core.msg import move
import rospy

class Robot(object):
    """docstring for Robot"""
    def __init__(self, robot_id, velocity, angular_velocity, x_offset, y_offset, theta_offset):
        super(Robot, self).__init__()
        self.robot_id = robot_id
        self.velocity = velocity
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.theta_offset = theta_offset
        self.odometry = ""
        self.is_moving = False
        
        def odometry_handler(data):
            """docstring for fname"""
            self.odometry = data

        rospy.Subscriber("/" + self.robot_id + "/odom", Odometry, odometry_handler)

    def forward(self, distance):
        """docstring for handle_position"""
        if not self.odometry == "":
            
            if not self.is_blocked() and not self.is_moving:
                publisher = rospy.Publisher("/" + self.robot_id + "/move", move, queue_size=10)
                p = self.get_position()
                x = distance * sin(p['theta'])
                y = distance * cos(p['theta'])
                x_normal = x * self.velocity / distance
                y_normal = y * self.velocity / distance

                msg = move()
                msg.x = x_normal
                msg.y = y_normal

                publisher.publish(msg)

        else:
            rate = rospy.Rate(10)
            rate.sleep()
            self.forward(distance)
    # def rotate(self, angle):
    #     """docstring for rotate"""
    #     if not self.odometry == "":
    #

    def get_position(self):
        """gets this robot's position relative to where it started"""
        position = self.odometry.pose.pose.position
        rotation = self.odometry.pose.pose.orientation
        return {
            'x': position.x + self.x_offset,
            'y': position.y + self.y_offset,
            'theta': rotation.z + self.theta_offset
        }

    def is_blocked(self):
        """is this robot able to move forward"""
        # TODO
        return False

