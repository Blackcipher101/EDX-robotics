#!/usr/bin/env python
import rospy
from project_0.msg import Two_ints

def talker():
    pub = rospy.Publisher('chatter', Two_ints, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = Two_ints()
    msg.x= 2
    msg.y = 9
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
    #rospy.spin()
if __name__ == "__main__":
    
     try:
        talker()
     except rospy.ROSInterruptException:
        pass