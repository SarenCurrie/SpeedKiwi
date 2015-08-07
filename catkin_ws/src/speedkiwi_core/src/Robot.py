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
        self.angular_velocity = angular_velocity
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

    def set_angular_velocity(self, speed):
        """Sets the twist message to include rotation at the given speed"""
        if not self.odometry == "":
            msg = Twist()
            msg.angular.z = speed
            self.velocity = msg
 

    def start_rotate(self):
        self.set_angular_velocity(self.angular_velocity)

    def start_rotate_opposite(self):
        self.set_angular_velocity(-self.angular_velocity)

    def rotate_at_speed(self, angular_speed):
        self.set_angular_velocity(angular_speed)

    def stop_rotate(self):
        self.set_angular_velocity(0)

    # TODO change these to require one call and exit when done (also more accuracy)
    def rotate_to_north(self):
        theta = self.position['theta']
        if not (theta < .05 and theta > -.05):
            self.start_rotate()
            print("Spin to north")
            return False
        else:
            self.stop_rotate()
            return True
        

    def rotate_to_south(self):
        theta = self.position['theta']
        if not (theta > .95 or theta < -.95):
            self.start_rotate()
            print("Spin to south")
            return False
        else:
            self.stop_rotate()
            return True

    def rotate_to_east(self):
        theta = self.position['theta']
        if not (theta > .45 and theta < .55):
            self.start_rotate()
            print("Spin to east")
            return False
        else:
            self.stop_rotate()
            return True

    def rotate_to_west(self):
        theta = self.get_position()['theta']

        if not (theta < -.45 and theta > -.55):
            self.start_rotate()
            print("Spin to west")
            return False
        else:
            self.stop_rotate()
            return True

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

    

    counter = 0
    spinning = False
    position = 0
    task_executing = False
    current_task = None

    def execute(self):
        """docstring for execute"""
        self.position = self.get_position()
        if not self.task_executing:
            self.execute_callback()
        self.execute_task()
        publisher = rospy.Publisher('/' + self.robot_id + '/cmd_vel', Twist, queue_size=100)
        publisher.publish(self.velocity)
        
        print (str(self.position['theta']) + " " + str(self.spinning))
        self.counter+=1

    def execute_callback(self):
        """To be overridden in extending classes"""
        #if not self.task_executing:
        if self.counter % 100 == 0 and not self.counter % 200 == 0:
            #self.spinning = True
            self.current_task = "rotate_to_west"
            self.task_executing = True

        if self.counter % 200 == 0:
            #self.spinning = False
            #self.start_rotate_opposite()
            self.current_task = "rotate_to_east"
            self.task_executing = True

        #self.execute_task()

        #if self.spinning == True:
        #    self.rotate_to_west()


        
        pass

    def execute_task(self):
        if self.current_task == "rotate_to_west":
            finished = self.rotate_to_west()

        elif self.current_task == "rotate_to_east":
            finished = self.rotate_to_east()

        if finished:
            self.task_executing = False