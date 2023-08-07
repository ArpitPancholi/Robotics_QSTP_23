#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
move = Twist()

while not rospy.is_shutdown():
    move.linear.x=0.2
    move.angular.z=0.0

    pub.publish(move)
    rospy.sleep(0.1)
