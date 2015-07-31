#!/usr/bin/env python

### ros python packages
import rospy
import ros

### ros messages
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

### access to stdin, stdout
import sys

### math libraries
import math


def StageOdom_callback( msg):

    #This is the call back function to process odometry messages coming from Stage.

    ### unsure how to unpack the msg fields at this point
    rospy.loginfo("message is: %s", msg)


def StageLaser_callback( msg):
    #This is the callback function to process laser scan messages
    # #you can access the range data from msg.ranges[i]. i = sample number
    pass


def main(argv):
    ### avoid globals - declare the robot variables in main.

    # pose of the robot
    theta = math.pi/2.0

    ### these need to get into the odometer callback but not sure how to do this yet
    px = 10
    py = 20

    # velocity of the robot
    linear_x = 0
    angular_z = 0

    ### equivalent to ros::init
    rospy.init_node('RobotNode1', argv, anonymous=True)
    rate = rospy.Rate(10)

    ### ok, each of these is a separate thread utilising the given callback.
    ### publishers have .publish invocation as a callback. subscribers have a user defined callback.
    node_stage_pub = rospy.Publisher("robot_1/cmd_vel", Twist, queue_size=1000)
    odo_stage_sub = rospy.Subscriber("robot_1/odom", Odometry, "StageOdom_callback")
    laser_stage_sub = rospy.Subscriber("robot_1/base_scan", LaserScan, "StageLaser_callback")
    count = 0

    twist_msg = Twist()

    while not rospy.is_shutdown():
        ### publish current velocities.
        twist_msg.linear.x = linear_x
        twist_msg.angular.z - angular_z

        node_stage_pub.publish(twist_msg)

        # there is no spinonce() method in rospy. a different approach is required
        # for action cycling?

        rate.sleep()
        count += 1


if __name__ == '__main__':
    main(sys.argv)


