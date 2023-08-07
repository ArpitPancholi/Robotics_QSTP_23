#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_forward_node')  
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

move = Twist()
move.linear.x = 0.2  

distance_to_move = 5.0  # goal distance

start_time = rospy.get_time()  

while not rospy.is_shutdown():
    pub.publish(move)
    
    # Calculate the distance moved based on time and velocity
    elapsed_time = rospy.get_time() - start_time
    distance_moved = elapsed_time * move.linear.x

    if distance_moved >= distance_to_move:
        move.linear.x = 0.0
        pub.publish(move)
        break

rospy.spin() 
