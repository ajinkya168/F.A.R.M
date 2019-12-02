#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32

def motor_start():
	pub=rospy.Publisher('motor_topic', Int32, queue_size = 10)
	motor_step=Int32()
	rate=rospy.Rate(10)

	while not rospy.is_shutdown():
		motor_step.data=input("enter the angle for motor=")
		pub.publish(motor_step)
		rospy.loginfo("angle is %d",motor_step.data)
if __name__=='__main__':
	try:
		rospy.init_node('motor',anonymous=True)
		motor_start()
	except rospy.ROSInterruptException: pass
