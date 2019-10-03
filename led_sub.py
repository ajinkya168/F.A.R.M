#! /usr/bin/env python

import rospy
import time
import RPi.GPIO as GPIO  
from std_msgs.msg import Int32     


GPIO.setmode(GPIO.BOARD)      
GPIO.setup(11, GPIO.OUT)      
def callback(data):
	while True:
	 if data.data== 1:
	  GPIO.output(11,True)
          rospy.loginfo("LED is turned on") 
	  time.sleep(1) 
	 if data.data== 0:   
	  GPIO.output(11,False)
          rospy.loginfo("LED is turned off")
	  time.sleep(1) 

def led_listner():
	rospy.Subscriber('led_topic', Int32 , callback)
        rospy.spin()

if __name__ == '__main__':
   rospy.init_node('led_sub', anonymous =True)
   led_listener()

