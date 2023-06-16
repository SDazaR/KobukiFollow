#!/usr/bin/env python3

import os
import rospy
import time

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan
import sensor_msgs.msg

def roundBy(x, base=5):
    return int(x) - int(x) % int(base)

def callback (msg):
	ang_min = 145
	ang_max = 215
	degrees = list(range(0, ang_max-ang_min))
	inten = list(msg.ranges[ang_min: ang_max])
	
	#inten = [20 if x == 0 else x for x in inten]
	inten = [1.0 if x > 1.0 else x for x in inten]

	inv_inten = list([max(inten)-x for x in inten])
	
	print (ang_max, ang_min, int((ang_max-ang_min)/2))
	try:
		direc = roundBy(sum(degrees[i]*inv_inten[i]for i in range(len(inten)))/sum(inv_inten),1)
	except:
		direc = int((ang_max-ang_min)/2)
		
	dist = sum(inten[direc-15:direc+15])/30

	#print(degrees) 
	print(inten) 
	print(direc, dist)
	

	
	ref_a = (ang_max-ang_min)/2
	ref_l = 0.6
	
	
	Kp_a = -0.09
	Kp_l = -0.4
	e_a = ref_a - direc
	e_l = ref_l - dist
	
	if e_l > 0:
		Kp_l = -0.8
	
	if Kp_a*e_a < -1.4:
		c_a = -1.4
	elif Kp_a*e_a > 1.4:
		c_a = 1.4
	else:
		c_a = Kp_a*e_a 
	
	if Kp_l*e_l < -0.15:
		c_l = -0.15
	elif Kp_l*e_l > 0.15:
		c_l = 0.15
	else:
		c_l = Kp_l*e_l
	 
	
	print (c_a, c_l)
	
	twist = Twist()
	twist.linear.x = c_l
	twist.angular.z = c_a
	vel_pub_.publish(twist)
	vel_pub_tur.publish(twist)

def listener():
	rospy.init_node("obst_direc_node")
	
	rate = rospy.Rate(10)
	
	global vel_pub_
	global vel_pub_tur
	vel_pub_ = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)
	vel_pub_tur = rospy.Publisher('turtle1/cmd_vel', Twist)
	rospy.Subscriber("/scan", LaserScan, callback)
	
	
	rospy.spin()


if __name__ == '__main__':
	listener()



		
