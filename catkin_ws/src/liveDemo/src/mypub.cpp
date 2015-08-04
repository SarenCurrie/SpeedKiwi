#include "ros/ros.h"
#include "liveDemo/my_msg.h"
#include "mylib.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv)
{
	ros::init(argc,argv,"mypub_node");
	
	ros::NodeHandle my_handle;

	ros::Publisher mypub_object = my_handle.advertise<geometry_msgs::Twist>("cmd_vel", 100);

	ros::Rate loop_rate(10);

	int counter = 0;

	while(ros::ok())
	{
		loop_rate.sleep();
		
		geometry_msgs::Twist mypub_msg; // replace existing similar assignments
		                mypub_msg.linear.x = 1;
						mypub_msg.linear.z = 0.1;
		                mypub_msg.angular.z = 0.5;

		mypub_object.publish(mypub_msg);
	}

	return 0;
}



