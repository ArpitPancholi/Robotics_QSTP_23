#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

PI = 3.14159265
dist_to_obj = 1
speed = 0.2
ang_speed = 0.3
angle = 90
rel_angle = 1.573

continue_moving = False  # Flag to control if the robot should continue moving

def rotateL():
    global move, ang_speed

    move.linear.x = 0
    move.linear.y = 0
    move.linear.z = 0
    move.angular.x = 0
    move.angular.y = 0
    move.angular.z = ang_speed

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < rel_angle:
        pub.publish(move)
        t1 = rospy.Time.now().to_sec()
        current_angle = ang_speed * (t1 - t0)
        
    # Forcing our robot to stop
    move.angular.z = 0
    pub.publish(move)


def rotateR():
    global move, ang_speed

    move.linear.x = 0
    move.linear.y = 0
    move.linear.z = 0
    move.angular.x = 0
    move.angular.y = 0
    move.angular.z = -1* ang_speed

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < rel_angle:
        pub.publish(move)
        t1 = rospy.Time.now().to_sec()
        current_angle = ang_speed * (t1 - t0)
        
    # Forcing our robot to stop
    move.angular.z = 0
    pub.publish(move)

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
move = Twist()

while not rospy.is_shutdown():
    alp = input("Enter the command (W: forward, a: rotate left, d: rotate right, s: stop): ")
    
    if alp == 'W' or alp == 'w':
        move.linear.x = 0.2
        move.angular.z = 0.0
        continue_moving = False

    elif alp == 'a' or alp == 'A':
        move.linear.x = 0.
        rotateL()           # Perform the turn
        move.angular.z = 0.0
        continue_moving = True

    elif alp == 'd' or alp == 'D':
        move.linear.x = 0.0
        rotateR()           # Perform the turn
        move.angular.z = 0.0
        continue_moving = True
    
    elif alp == 'S' or alp == 's':
        move.linear.x = 0
        move.linear.y = 0
        move.linear.z = 0
        move.angular.x = 0
        move.angular.y = 0
        move.angular.z = 0
        continue_moving = False

    if continue_moving:
        move.linear.x = 0.2  # Set linear motion if continue_moving is True

    pub.publish(move)
    rospy.sleep(0.1)
