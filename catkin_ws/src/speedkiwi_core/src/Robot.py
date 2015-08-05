from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
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
        self.odometry = None
        self.velocity = Twist()
        self.is_moving = False
        
        def odometry_handler(data):
            """docstring for fname"""
            self.odometry = data

        rospy.Subscriber("/" + self.robot_id + "/odom", Odometry, odometry_handler)

        # Wait for odometry datax`
        while self.odometry is None:
            print("waiting")

    def forward(self):
        """starts the robot moving at it's top speed"""
        self.set_velocity(self.top_speed)

    def stop(self):
        """Stops the robot from moving"""
        self.set_velocity(0)

    def set_velocity(self, linear):
        """docstring for set_velocity"""
        if not self.odometry is None:
            if not self.is_blocked() and not self.is_moving:
                msg = Twist()
                msg.linear.x = linear
                self.velocity = msg

    def set_angular_velocity(self):
        """docstring for set_angular_velocity"""
        # TODO


    def rotate(self, angle):
        """docstring for rotate"""
        if not self.odometry == "":
            msg = Twist()
            msg.angular.z = angle
            self.velocity = msg

    def start_rotate(self):
        self.rotate(self.angular_velocity)

    def start_rotate_opposite(self):
        self.rotate(-self.angular_velocity)

    def stop_rotate(self):
        self.rotate(0)

    # TODO 
    def rotate_to_north(self):
        stuff = self.get_position()
        stuff2 = stuff['theta']
        if stuff2 < .5 or (stuff2 > -.5 and stuff2 < 0):
            self.start_rotate_opposite()
            print("Stuck")
        else:
            self.stop_rotate()
        
        print(str(stuff['theta']) + 'word')

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
        self.execute_callback()
        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)

    def execute_callback(self):
        """To be overridden in extending classes"""
        stuff = self.get_position()
        print (stuff['theta'])
        pass