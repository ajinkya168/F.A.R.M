#!/usr/bin/env python


import rospy   #import rospy 
from std_msgs.msg import Int32  #import Int32 msg from std_msgs package


def led_start():
     pub=rospy.Publisher('led_topic', Int32, queue_size=10)      #create a object to publish data
     led_cmd = Int32()     #create a constructor for msg
      
     rate=rospy.Rate(10)
                         
     while not rospy.is_shutdown():                    #run the loop until its not terminated
         led_cmd.data = input("Enter command for led =")   #taking input from user                                                      
         pub.publish(led_cmd)                                #publish data to topic                  
         rospy.loginfo("Sending command %d.....",led_cmd.data)
         if (led_cmd.data == 1):
          rospy.loginfo("Command %d is sent!Check your LED!", led_cmd.data)    #if command 1 is true
         elif(led_cmd.data == 0):
          rospy.loginfo("Command %d is sent! LED is off now!",led_cmd.data)    #if command 0 is true
         else :
          rospy.loginfo("Error:Recheck your command!LED doesn't recognize!")#if numbers except 1 and 0 is given
          break                        
          rate.sleep()



if __name__  == '__main__':
 try: 
    rospy.init_node('led', anonymous = True)   #initialize node
    led_start()                          #call function led_start()                   
 except rospy.ROSInterruptException: pass
        

    
