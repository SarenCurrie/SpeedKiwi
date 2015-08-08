from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from math import sin, cos
import rospy
import tf 
from tf.transformations import euler_from_quaternion

class Robot(object):

    """
    Provides a generic class to represent robots and other objects in stage.
    Stage only allows robots initialised in the world file to be manipulated by ROS,
    therefore we have to initialise the robots in the world file as well as this class.
    """

    NO_ACTION = Action()
    counter = 0
    pi = 3.14159265359

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
        self.angular_velocity = angular_velocity
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.theta_offset = theta_offset
        self.odometry = None
        self.velocity = Twist()
        self.is_moving = False
        self._action_queue = []
        self.rotation_executing = False
        self.current_rotation = None
        
        def odometry_handler(data):
            """docstring for fname"""
            self.odometry = data

        rospy.Subscriber("/" + self.robot_id + "/odom", Odometry, odometry_handler)

        # Wait for odometry datax`
        while self.odometry is None:
            print("waiting")

        self.position = self.get_position()

    def forward(self):
        """starts the robot moving at it's top speed"""
        self.set_linear_velocity(self.top_speed)

    def stop(self):
        """Stops the robot from moving"""
        self.set_linear_velocity(0)

    def set_linear_velocity(self, linear):
        """docstring for set_velocity"""
        if not self.odometry is None:
            msg = Twist()
            msg.linear.x = linear
            self.velocity = msg

    def set_angular_velocity(self, speed):
        """Sets the twist message to include rotation at the given speed"""
        if not self.odometry == "":
            msg = Twist()
            msg.angular.z = speed
            self.velocity = msg
 

    def start_rotate(self):
        """Sets rotation to speed definied in constructor (anti clockwise) """
        self.set_angular_velocity(self.angular_top_speed)

    def start_rotate_opposite(self):
        """Sets rotation to speed definied in constructor (clockwise) """
        self.set_angular_velocity(-self.angular_top_speed)

    def stop_rotate(self):
        """Stops the robot from rotating"""
        self.set_angular_velocity(0)

    def rotate_to_north(self): # NOTE: north is defined in the direction of the positive x axis
        """Sets the rotation until the robot is facing north
        Returns true if facing north (false otherwise)"""
        theta = self.position['theta']
        if not (theta < .1 and theta > -.1):
            self.start_rotate()
            print("Spin to north")
            return False
        else:
            self.stop_rotate()
            return True

    def rotate_to_south(self):
        """Sets the rotation until the robot is facing south
        Returns true if facing south (false otherwise)"""
        theta = self.position['theta']
        if not (theta > (self.pi-.1) or theta < (-self.pi+.1)):
            self.start_rotate()
            print("Spin to south")
            return False
        else:
            self.stop_rotate()
            return True

    def rotate_to_west(self):
        """Sets the rotation until the robot is facing west
        Returns true if facing west (false otherwise)"""
        theta = self.position['theta']
        if not (theta > ((self.pi/2)-.1) and theta < ((self.pi/2)+.1)):
            self.start_rotate()
            print("Spin to west")
            return False
        else:
            self.stop_rotate()
            return True

    def rotate_to_east(self):
        """Sets the rotation until the robot is facing east
        Returns true if facing east (false otherwise)"""
        theta = self.get_position()['theta']

        if not (theta < (-(self.pi/2)+.1) and theta > (-(self.pi/2)-.1)):
            self.start_rotate()
            print("Spin to east")
            return False
        else:
            self.stop_rotate()
            return True

    def get_position(self):
        """gets this robot's position relative to where it started"""
        position = self.odometry.pose.pose.position
        rotation = self.odometry.pose.pose.orientation
        euler = euler_from_quaternion(quaternion=(rotation.x, rotation.y, rotation.z, rotation.w)) # Convert to usable angle
        return {
            'x': position.x + self.x_offset,
            'y': position.y + self.y_offset,
            'theta': euler[2] + self.theta_offset
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
        action = self.NO_ACTION
        if self._action_queue:
            action = self._action_queue[0]
            if action.is_finished(self):
                action.finish(self)
                self._action_queue.remove(action)
                if self._action_queue:
                    action = self._action_queue[0]
                    action.start(self)
                else:
                    action = self.NO_ACTION
        action.during(self)

        self.position = self.get_position()
        # if not self.rotation_executing: # If already doing something just continue doing it
        #     self.execute_callback()
        # self.execute_rotation()

        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)
        
        print (str(self.position['theta']))
        self.counter+=1

        # print (str(self.position['theta']))

    def execute_callback(self):
        """To be overridden in extending classes to define behaviours for each robot."""

        # if self.counter % 100 == 0 and not self.counter % 200 == 0:
        #     self.current_rotation = "rotate_to_north"
        #     self.rotation_executing = True
        #
        # if self.counter % 200 == 0:
        #     self.current_rotation = "rotate_to_south"
        #     self.rotation_executing = True
        #
        pass

    def perform_rotation(self):
        """If a rotation has been started but not finished it will be executed each 'tick'"""
        # finished = False
        # if self.current_rotation == "rotate_to_west":
        #     finished = self.rotate_to_west()
        # elif self.current_rotation == "rotate_to_east":
        #     finished = self.rotate_to_east()
        # elif self.current_rotation == "rotate_to_north":
        #     finished = self.rotate_to_north()
        # elif self.current_rotation == "rotate_to_south":
        #     finished = self.rotate_to_south()
        # if finished:
        #     self.is_rotating = False

