#include "ros/ros.h"
#include "liveDemo/my_msg.h"

void mypubCallback(const liveDemo::my_msg::ConstPtr& msg)
{
	ROS_INFO("sub echoing pub: %d",msg->my_counter);
}

int main(int argc, char **argv)
{
	ros::init(argc,argv,"mysub_node");
	
	ros::NodeHandle my_handle;

	ros::Subscriber mysub_object = my_handle.subscribe("mypub_topic", 100, mypubCallback);

	ros::spin();

	return 0;
}



