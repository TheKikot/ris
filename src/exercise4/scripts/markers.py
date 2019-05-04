import roslib
roslib.load_manifest('exercise4')
import rospy
import sensor_msgs.msg
import message_filters
import tf2_ros
from std_msgs.msg import String, Bool, ColorRGBA
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Vector3
