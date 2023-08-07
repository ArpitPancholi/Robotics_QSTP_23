#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


dist_to_obj = 0.1
speed = 0.2

forward_distance = 10.0  

def callback(msg):
    global forward_distance

    forward_distance = msg.ranges[0]  

    rospy.loginfo("The distance from the obstacle is {:.2f}".format(forward_distance))      #Prints the forward distance

    if forward_distance < dist_to_obj:
        rospy.loginfo("Object Detected")                                                    #Prints object detected if objectdistance<=0.1

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
sub = rospy.Subscriber('/scan', LaserScan, callback)
move = Twist()

while not rospy.is_shutdown():
    if forward_distance > dist_to_obj:
        move.linear.x = 0.2
        move.angular.z = 0.0

    else:
        move.linear.x = 0.0           
        move.angular.z = 0.0

    
    pub.publish(move)
    rospy.sleep(0.1)
