from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import rospy

class Robot(object):
    """
    Provides a generic class to represent robots and other objects in stage.
    Stage only allows robots initialised in the world file to be manipulated by ROS,
    therefore we have to initialise the robots in the world file as well as this class.
    """
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        """
        robot_id: The robot's name in stage
        top_speedL The robot's maximum speed
        x_offset: The x coordinate the robot starts at in stage
        y_offset: The y coordinate the robot starts at in stage
        theta_offset: The direction this robot starts facing in stage
        """
        super(Robot, self).__init__()
        self.robot_id = robot_id
        self.top_speed = top_speed
        self.angular_top_speed = angular_top_speed
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.theta_offset = theta_offset
        self.odometry = None
        self.velocity = Twist()
        self.is_moving = False
        
        def odometry_handler(data):
            """
            Handles odometry messages from stage
            """
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
        """Sets the robot's velocity in m/s"""
        if not self.odometry is None:
            if not self.is_blocked():
                msg = Twist()
                msg.linear.x = linear
                self.velocity = msg

    def set_angular_velocity(self, angular):
        """docstring for set_angular_velocity"""
        # TODO

    # def rotate(self, angle):
    #     """docstring for rotate"""
    #     if not self.odometry == "":
    #

    def get_position(self):
        """gets this robot's position"""
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
        """
        To be called by the ros loop. This method sends the Twist message to stage.
        This method should not be overridden instead use execute_callback()
        """
        self.execute_callback()
        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)

    def execute_callback(self):
        """To be overridden in extending classes to define behaviours for each robot."""
        pass
