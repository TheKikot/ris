#include "ros/ros.h"
#include "pck2/sum.h"
#include <stdlib.h>
#include <string.h>

#include <string>
#include <iostream>

bool manipulate(pck2::sum::Request  &req,
         pck2::sum::Response &res)
{

  int sum = 0;
  for(std::vector<int>::iterator it = req.content.begin(); it != req.content.end(); ++it)
    sum += *it;

  ROS_INFO("%d", sum);
  //ROS_INFO("%s", typeid(req.content).name());
  /*char *str = (char*)req.content.c_str();
  char *pch;
  pch = strtok(req.content, " ");
  int sum = 0;
  while(pch != NULL)
  {
	int currNum = atoi(pch);
	sum += currNum;
	pch = strtok(NULL, " ");
  }

  res.comment = itoa(sum, res.comment, 10);

  ROS_INFO("request: %s, response: %s", req.content.c_str(), res.comment.c_str());
  return true;*/
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "our_service_node");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("our_service_node/string", manipulate);
  ROS_INFO("I am ready to mess up your string!");
  ros::spin();

  return 0;
}
