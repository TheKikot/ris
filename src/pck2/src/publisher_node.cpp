#include <ros/ros.h> // As previously said the standard ROS library
#include "std_msgs/String.h"
#include "pck2/homework_message.h"

#include <sstream>

int main(int argc, char *argv[])
{
	ros::init(argc,argv,"publisher"); //Initialize the ROS system, give the node the name "publish_velocity"
	ros::NodeHandle nh;	//Register the node with the ROS system

	//create a publisher object.
	ros::Publisher pub = nh.advertise<pck2::homework_message>("pub/chat", 1000);	//the message tyoe is inside the angled brackets
																						//topic name is the first argument
																						//queue size is the second argument


	//Loop at 2Hz until the node is shutdown.
	ros::Rate rate(0.1);
	
	int count = 0;
	while(ros::ok()){
		//Create the message.
		pck2::homework_message msg;

		std::stringstream ss;

		ss << "hello custom messaging world";
		msg.content=ss.str();
		msg.number=count;
		count++;
		//msg.count=seq;

		//Publish the message
		pub.publish(msg);

		//Send a message to rosout
		ROS_INFO("%s", msg.content.c_str());

		//Wait untilit's time for another iteration.
		rate.sleep();
	}

	return 0;
}
