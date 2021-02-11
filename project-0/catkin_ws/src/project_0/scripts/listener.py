#!/usr/bin/env python
import rospy
from project_0.msg import Two_ints
from std_msgs.msg import Int32
pub =None
def callback(msg):
    sumofvalues=msg.x+msg.y
    pub.publish(sumofvalues)
    print("doing")

def talker():
    global pub
    rospy.init_node('listener', anonymous=True)
    pub = rospy.Publisher('/sum', Int32, queue_size=10)
    sub = rospy.Subscriber('/chatter', Two_ints, callback)
    
    rospy.spin()
if __name__ == "__main__":
    
     try:
        talker()
     except rospy.ROSInterruptException:
        pass