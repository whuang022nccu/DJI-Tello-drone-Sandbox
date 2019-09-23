import rospy
from geometry_msgs.msg import Twist

def turtle_pub():

    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('turtlesim_pub',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg =Twist()
        msg.linear.x=2.0
        msg.angular.z=-1.8
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
if __name__ == "__main__":
    try:
        turtle_pub()
    except rospy.ROSInterruptException:
        pass
    