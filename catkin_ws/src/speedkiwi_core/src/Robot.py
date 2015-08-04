from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import rospy

class Robot(object):
    """docstring for Robot"""
    def __init__(self, robot_id):
        super(Robot, self).__init__()
        self.robot_id = robot_id
        self.odometry = ""

        def odometry_handler(data):
            """docstring for fname"""
            self.odometry = data
        rospy.Subscriber(self.robot_id + "/odom", Odometry, odometry_handler)

    def forward(self, distance):
        """docstring for handle_position"""
        if not self.odometry == "":
            pub = rospy.Publisher('topic', String, queue_size=10)

            if not self.is_blocked():
                p = self.get_position()
                r = self.get_rotation()
#                 pub.publish(p.x)
#                 pub.publish(p.y)
#                 pub.publish(p.z)
#                 pub.publish(r.x)
#                 pub.publish(r.y)
#                 pub.publish(r.z)
                print(p.x)
                print(p.y)
                print(p.z)
                print(r.x)
                print(r.y)
                print(r.z)

    def get_position(self):
        """gets this robot's position relative to where it started"""
        return self.odometry.pose.pose.position

    def get_rotation(self):
        """gets this robot's rotation relative to where it started"""
        return self.odometry.pose.pose.orientation

    def is_blocked(self):
        """is this robot able to move forward"""
        # TODO
        return False

