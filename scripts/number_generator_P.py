#!/user/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

def random_int():
    return random.randint(1,1000)

if __name__ == "__main__":
    rospy.init_node('number_generator_P')
    pub=rospy.Publisher("random_number",Int32,queue_size=10)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        random_numbers=random_int()
        pub.publish(random_numbers)
        rate.sleep()
