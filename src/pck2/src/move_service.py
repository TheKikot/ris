#!/usr/bin/env python

import random
import rospy
from pck2.srv import movesrv
from geometry_msgs.msg import Twist

last_shape = "none"
speed = 5

def random_movement(step):
	
	twist = Twist()
	twist.linear.x = random.uniform(0.0,2.0)*speed
	twist.angular.z = random.uniform(-3.14,3.14)

	return twist

def rectangle_movement(step):

  twist = Twist()
  twist.linear.x = 0.1*speed
  step = step % 20

  if step % 5 == 0:
    twist.linear.x = 0
    twist.angular.z = 1.57 #(90 / 360) * 2 * 3.14

  return twist

def triangle_movement(step):

  twist = Twist()
  twist.linear.x = 0.1*speed
  step = step % 15

  if step % 5 == 0:
    twist.linear.x = 0
    twist.angular.z = 2.09 #(120 / 360) * 2 * 3.14

  return twist
  
def circle_movement(step):

  twist = Twist()
  twist.linear.x = 0.3*speed
  twist.angular.z = 0.3*speed	#(1 / 360) * 2 * 3.14

  return twist
  
def movement(shape, time):
	pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 1000)
	# For the turtle simulation map the topic to /turtle1/cmd_vel
	# For the turtlebot simulation and Turtlebot map the topic to /cmd_vel_mux/input/navi
	#rospy.init_node('movement')
	
	# we will be changing the last_shape variable
	global last_shape
	
	# assign the right function
	if shape == 'rectangle':
		move_fun = rectangle_movement
	elif shape == 'triangle':
		move_fun = triangle_movement
	elif shape == 'circle':
		move_fun = circle_movement
	else:
		move_fun = random_movement

	freq = 1
	r = rospy.Rate(freq)

	step = 0.0

	while step <= time*freq:
		twist = move_fun(step)
		step = step + 1.0
		pub.publish(twist)
		r.sleep()
		
	last_shape = shape

def move_server_function(req):
    #print("Shape: " + req.shape)
    #print("TIME: " + (str)req.time)
    movement(req.shape, req.time)
    return last_shape

def move_service():
    rospy.init_node('move_service')
    s = rospy.Service('move', movesrv, move_server_function)
    print "Ready to move."
    rospy.spin()

if __name__ == "__main__":
    move_service()
