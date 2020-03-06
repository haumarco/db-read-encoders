#!/usr/bin/env python

import os
import rospy
from duckietown import DTROS
from read_encoders.msg import encoderTicksStamped
from std_msgs.msg import Header
import pigpio
#from std_msgs.msg import String


#marco
from duckietown_msgs.msg import WheelsCmdStamped
import numpy as np

# Global
#pi = 3.14
pi = pigpio.pi()
cb_left = pi.callback(18, pigpio.RISING_EDGE)
cb_right = pi.callback(19, pigpio.RISING_EDGE)


class MyNode(DTROS):

	def __init__(self, node_name):
		# initialize the DTROS parent class
		super(MyNode, self).__init__(node_name=node_name)
		# construct publisher
		self.pub = rospy.Publisher('encoder_ticks', encoderTicksStamped, queue_size=1)
		# Note: Update to include to islduckie44/wheels_driver_node/wheels_cmd_executed to check the direction of the wheels 
		# ... so the encoder ticks can be incremented or decremented
		self.msg = encoderTicksStamped() # Following the Duckietown convention

		# setup for getting wheel direction
		self.lastcb_left = 0
		self.lastcb_right = 0
		self.wheel_dir_left = WheelsCmdStamped()
		self.wheel_dir_right = WheelsCmdStamped()
		self.sub_wheel_dir =rospy.Subscriber("wheels_driver_node/wheels_cmd_executed", WheelsCmdStamped, self.update_wheel_direction, queue_size=1)



		# Relate pi to the pigpio interface
		self.pi = pigpio.pi()

		self.left_motor_pin = 18
		self.right_motor_pin = 19

		# Setup the callbacks for each io pin
		global cb_left
		global cb_right
		cb_left = self.pi.callback(self.left_motor_pin, pigpio.RISING_EDGE, self.cbPublish())
		cb_right = self.pi.callback(self.right_motor_pin, pigpio.RISING_EDGE, self.cbPublish())

		rospy.loginfo("%s has finished initializing!" % node_name)


	# updates wheel direction of each wheel
	def update_wheel_direction(self, msg_wheel_dir):
		if (msg_wheel_dir.vel_left != 0):
			self.wheel_dir_left = msg_wheel_dir.vel_left
		if (msg_wheel_dir.vel_right != 0):
			self.wheel_dir_right = msg_wheel_dir.vel_right


	def cbPublish(self):
		# Publishes both sets of encoder ticks whenver a tick is registered
		global cb_left
		global cb_right

		# Form the message
		# Difference of ticks since the last published value
		self.msg.header.stamp = rospy.get_rostime()
		self.msg.left_ticks = (cb_left.tally() - self.lastcb_left) * np.sign(self.wheel_dir_left)
		self.msg.right_ticks = (cb_right.tally() - self.lastcb_right) * np.sign(self.wheel_dir_right)

		# Publish the message
		self.pub.publish(self.msg)

		rospy.loginfo("Published %s %s" % (self.msg.left_ticks, self.msg.right_ticks)) # Diagnostic - comment this out to reduce CPU usage.


	def run(self):

		rospy.loginfo("Encoder ticks node has reached the main run function and is running")

		# publish messagehttps://www.google.com/search?q=import+numpy&client=ubuntu&hs=1eq&channel=fs&tbm=isch&source=iu&ictx=1&fir=-FcoxcAhv5quKM%253A%252CseZ5QRd8Ko_0VM%252C_&vet=1&usg=AI4_-kS67HWs6cydc2cyF9iDnInV6H8gZA&sa=X&ved=2ahUKEwj0iMOYioPoAhWmyqYKHRCHCNQQ9QEwAHoECAQQAw#imgrc=-FcoxcAhv5quKM:s corresponding the frequency
		rate = rospy.Rate(5) # Hz - User can adjust this.
		# self.msg = encoderTicksStamped() # Defined in __init__

		# Establish timing for reporting rospy.loginfo updates
		#now = rospy.get_rostime()
		#secs = now.secs
		#wait_time = 1


		global cb_left
		global cb_right
		self.lastcb_left = cb_left.tally()
		self.lastcb_right = cb_right.tally()




		while not rospy.is_shutdown():
			if ((cb_left.tally() != self.lastcb_left) or (cb_right.tally() != self.lastcb_right)):
				self.pi.callback(self.left_motor_pin,  pigpio.RISING_EDGE, self.cbPublish())
				self.lastcb_left = cb_left.tally()
				self.lastcb_right = cb_right.tally()


			rate.sleep()




if __name__ == '__main__':
	# create the node
	node = MyNode(node_name='my_node')
	# run node
	node.run()
	# keep spinning
	rospy.spin()
