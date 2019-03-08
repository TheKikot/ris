#include "ros/ros.h"
#include "pck2/sum.h"

//#include <cstdlib>
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "our_client_node");
  ros::NodeHandle n;

  ros::ServiceClient client = n.serviceClient<pck2::sum>("our_service_node/string");

  pck2::sum srv;

  std::vector<int> ss(10);

  for(int i = 0; i < 10; i++){
	ss[i] = rand() % 10;
  }

  srv.request.content = ss;

  ros::service::waitForService("our_service_node/string", 1000);

  //ROS_INFO("Sending: %s", srv.request.content.c_str());

  if (client.call(srv))
  {
    ROS_INFO("The service returned: %d", srv.response.comment);
  }
  else
  {
    ROS_ERROR("Failed to call service");
    return 1;
  }

  return 0;
}
