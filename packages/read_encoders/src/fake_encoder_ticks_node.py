#!/usr/bin/env python

import os
import rospy
from duckietown import DTROS
from read_encoders.msg import encoderTicksStamped
from std_msgs.msg import Header, Int32
#from std_msgs.msg import String


class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name)
        # construct publisher
        self.pub = rospy.Publisher('encoder_ticks', encoderTicksStamped, queue_size=1)
	self.msg = encoderTicksStamped() # Following the Duckietown convention

    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(10) # Hz
	# self.msg = encoderTicksStamped() # Defined in __init__

	# Establish timing for reporting rospy.loginfo updates
        now = rospy.get_rostime()
        secs = now.secs
        wait_time = 1
	ticks = 0

        while not rospy.is_shutdown():
            self.msg.header.stamp = rospy.get_rostime()
            self.msg.left_ticks = ticks
            self.msg.right_ticks = ticks+1
            #rospy.loginfo("Publishing message: ")
            #rospy.loginfo(self.msg)
            self.pub.publish(self.msg)
            ticks += 1
	    # Update to console and adjust current time "secs"
#            if((rospy.get_rostime().secs - secs) > wait_time):
#		rospy.loginfo("Fake ticks: %d" % (ticks) )
#		now = rospy.get_rostime()
#		secs = now.secs

            rate.sleep()




if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node')
    # run node
    node.run()
    # keep spinning
    rospy.spin()
