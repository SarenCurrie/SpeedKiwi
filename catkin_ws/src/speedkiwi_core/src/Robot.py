from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
from speedkiwi_core.msg import move
import rospy

class Robot(object):
    """docstring for Robot"""
    def __init__(self, robot_id, top_speed, angular_velocity, x_offset, y_offset, theta_offset):
        super(Robot, self).__init__()
        self.robot_id = robot_id
        self.top_speed = top_speed
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.theta_offset = theta_offset
        self.odometry = ""
        self.velocity = Twist()
        self.is_moving = False
        
        def odometry_handler(data):
            """docstring for fname"""
            self.odometry = data

        rospy.Subscriber("/" + self.robot_id + "/odom", Odometry, odometry_handler)

        # Wait for odometry data
        while self.odometry == "":
            # wait
            print("waiting")

    def forward(self, distance):
        """docstring for handle_position"""
        if not self.odometry == "":
            
            if not self.is_blocked() and not self.is_moving:
                # publisher = rospy.Publisher("/move", move, queue_size=10)
                p = self.get_position()
                x = distance * sin(p['theta'])
                y = distance * cos(p['theta'])
                x_normal = x * self.top_speed / distance
                y_normal = y * self.top_speed / distance

                msg = Twist()
                msg.linear.x = self.top_speed
                # msg.y = y_normal
                self.velocity = msg

                # publisher.publish(msg)

                print("set velocity " + str(x_normal))

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

    def execute(self):
        """docstring for execute"""
        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)