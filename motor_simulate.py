#! /usr/bin/env python
import rospy
from sensor.msgs import JointState
from time import sleep
import RPi.GPIO as GPIO
import numpy

DIR = 12
STEP =5
CW = 1
CCW = 0
EN=8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
#GPIO.setup(M0, GPIO.OUT)
#GPIO.setup(M1, GPIO.OUT)
#GPIO.setup(M2, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

delay=0.0005

GPIO.output(EN, GPIO.LOW)

def joint_states_callback(message):

    message.position=(message.position*180)/3.14
    
    for i in range(len(message.position)):
            	if message.position > 0:                                                ##FOR CLOCKWISE DIRECTION
                rospy.loginfo("running  %s motor %f cm forward", message.name, message.position)
		step_count=(message.position)/1.8
		rospy.loginfo(step_count)		
		for x in numpy.arrange((step_count)):
			GPIO.output(EN, GPIO.LOW)
			GPIO.output(DIR, GPIO.HIGH)
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)			
			sleep(delay)
			GPIO.output(EN,GPIO.HIGH)
 
            	elif message.position < 0:                                                ##FOR CLOCKWISE DIRECTION
                rospy.loginfo("running  %s motor %f cm forward", message.name, message.position)
		step_count=(message.position)/1.8
		rospy.loginfo(step_count)		
		for x in numpy.arrange((step_count)):
			GPIO.output(EN, GPIO.LOW)
			GPIO.output(DIR, GPIO.LOW)
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)			
			sleep(delay)
			GPIO.output(EN,GPIO.HIGH)

                GPIO.output(EN,GPIO.HIGH)

if __name__ == '__main__':
    rospy.init_node("joint_pose")
    rospy.Subscriber("/arm_controller/joint_states", JointState, joint_states_callback, queue_size=1)
    rospy.spin()
