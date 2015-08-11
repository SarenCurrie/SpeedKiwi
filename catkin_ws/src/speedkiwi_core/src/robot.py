import rospy
import tf
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from rosgraph_msgs.msg import Log
from math import sin, cos
from action import Action
from tf.transformations import euler_from_quaternion
from math import pi


class Robot(object):
    """Provides a generic class to represent robots and other objects in stage.

    Stage only allows robots initialised in the world file to be manipulated by ROS,
    therefore we have to initialise the robots in the world file as well as this class.
    """

    NO_ACTION = Action()

    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        """
        robot_id: The robot's name in stage
        top_speed: The robot's maximum speed
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
        self.laser = None
        self._action_queue = []
        self.rotation_executing = False
        self.current_rotation = None

        def odometry_handler(data):
            """
            Handles odometry messages from stage
            """
            self.odometry = data

        rospy.Subscriber("/" + self.robot_id + "/odom", Odometry, odometry_handler)

        def scan_handler(data):
            """
            Handles LaserScan messages from stage
            """
            self.laser = data

        rospy.Subscriber("/" + self.robot_id + "/base_scan", LaserScan, scan_handler)

        # Wait for odometry data
        while self.odometry is None:
            rospy.loginfo("Waiting for odometry information")

        self.position = self.get_position()

    def forward(self):
        """starts the robot moving at it's top speed"""
        self.set_linear_velocity(self.top_speed)

    def stop(self):
        """Stops the robot from moving"""
        self.set_linear_velocity(0)
        self.rotation_executing = False

    def set_linear_velocity(self, linear):
        """Sets this robot's velocity in m/s"""
        if self.odometry is not None:
            msg = Twist()
            msg.linear.x = linear
            self.velocity = msg

    def set_angular_velocity(self, angular):
        """Sets the twist message to include rotation at the given speed"""
        if self.odometry is not None:
            msg = Twist()
            msg.angular.z = angular
            self.velocity = msg

    def start_rotate(self):
        """Sets rotation to speed definied in constructor (anti clockwise) """
        self.set_angular_velocity(self.angular_top_speed)
        self.rotation_executing = True

    def start_rotate_opposite(self):
        """Sets rotation to speed definied in constructor (clockwise) """
        self.set_angular_velocity(-self.angular_top_speed)
        self.rotation_executing = True

    def stop_rotate(self):
        """Stops the robot from rotating"""
        self.set_angular_velocity(0)
        self.rotation_executing = False

    def rotate_to_east(self): 
        """Sets the rotation until the robot is facing east
        Returns true if facing east (false otherwise)"""
        return self.rotate_to_angle(0)

    def rotate_to_west(self):
        """Sets the rotation until the robot is facing west
        Returns true if facing west (false otherwise)"""
        theta = self.position['theta']
        if (theta < ((-pi)+.0001) or theta > (pi-.0001)):
            self.stop_rotate()
            return True
        elif (theta < ((-pi)+.003) and theta > -pi):
            self.set_angular_velocity(-self.angular_top_speed/500)
        elif (theta > (pi-.003) and theta < pi):
            self.set_angular_velocity(self.angular_top_speed/500)
        elif (theta < ((-pi)+.03) and theta > -pi):
            self.set_angular_velocity(-self.angular_top_speed/100)
        elif (theta > (pi-.03) and theta < pi):
            self.set_angular_velocity(self.angular_top_speed/100)
        elif (theta < ((-pi)+.3) and theta > -pi):
            self.set_angular_velocity(-self.angular_top_speed/4)
        elif (theta > (pi-.3) and theta < pi):
            self.set_angular_velocity(self.angular_top_speed/4)
        elif (theta >= 0):
            self.start_rotate()
        else:
            self.start_rotate_opposite()
            return False

    def rotate_to_north(self): # NOTE: north is defined in the direction of the positive y axis
        """Sets the rotation until the robot is facing north
        Returns true if facing north (false otherwise)"""
        return self.rotate_to_angle(pi/2)

    def rotate_to_south(self):
        """Sets the rotation until the robot is facing south
        Returns true if facing south (false otherwise)"""
        return self.rotate_to_angle(-pi/2)

    def rotate_to_angle(self, target):
        """Rotates to the desired target angle. Returns true when facing that direction"""
        theta = self.position['theta']
        if target == pi or target == -pi:
            return rotate_to_west()
        if (theta < (target+.0001) and theta > (target-.0001)):
            self.stop_rotate()
            return True
        elif (theta < (target+.003) and theta > target):
            self.set_angular_velocity(-self.angular_top_speed/500)
        elif (theta > (target-.003) and theta < target):
            self.set_angular_velocity(self.angular_top_speed/500)
        elif (theta < (target+.03) and theta > target):
            self.set_angular_velocity(-self.angular_top_speed/100)
        elif (theta > (target-.03) and theta < target):
            self.set_angular_velocity(self.angular_top_speed/100)
        elif (theta < (target+.3) and theta > target):
            self.set_angular_velocity(-self.angular_top_speed/4)
        elif (theta > (target-.3) and theta < target):
            self.set_angular_velocity(self.angular_top_speed/4)
        elif ((target >= 0) and (theta > (target-pi)) and (theta < target)) or ((target <= 0) and not ((theta < (target+pi)) and (theta > target))):
            self.start_rotate()
        else:
            self.start_rotate_opposite()
            return False

    def get_position(self):
        """gets this robot's position"""
        position = self.odometry.pose.pose.position
        rotation = self.odometry.pose.pose.orientation
        # Convert to usable angle
        euler = euler_from_quaternion(quaternion=(rotation.x, rotation.y, rotation.z, rotation.w))
        theta = euler[2] + self.theta_offset
        if theta < -pi:
            theta = theta + (2*pi)
        elif theta > pi:
            theta = theta - (2*pi)
        return {
            'x': position.x + self.x_offset,
            'y': position.y + self.y_offset,
            'theta': theta
        }

    def is_blocked(self):
        """is this robot able to move forward"""
        if self.laser:
            for range in self.laser.ranges:
                if range < 2:
                    rospy.logdebug(str(range))
                    return True
        return False

    def add_action(self, action):
        """Adds an action to this robot's action queue"""
        self._action_queue.append(action)

    def execute(self):
        """
        To be called by the ros loop. This method sends the Twist message to stage.
        This method should not be overridden instead use execute_callback()
        """
        self.position = self.get_position()
        #rospy.loginfo(self.position["theta"])

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


        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)

    def execute_callback(self):
        """To be overridden in extending classes to define behaviours for each robot."""
        pass
