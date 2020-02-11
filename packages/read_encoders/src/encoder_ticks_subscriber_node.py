#!/usr/bin/env python

# Do not call this node or function unless you need a diagnostic check.
# This node will publish the number of left and right encoder ticks for diagnostic purposes
# but does not do anything meaningful, other than to log them to the screen.

import os
import rospy
from duckietown import DTROS
from std_msgs.msg import Header, Int32
from read_encoders.msg import encoderTicksStamped

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name)
        # construct subscriber
        self.sub = rospy.Subscriber("encoder_ticks", encoderTicksStamped, self.cbPrint)
	#rospy.spin()
	rospy.loginfo("%s has started!" % node_name)

    def cbPrint(self, msg):
	# This callback function is partially diagnostic and will report whether
	# any encoder tick messages have been published.


        #rospy.loginfo("I heard something:" )
	rospy.loginfo("Sub: Left ticks: %d \t Right ticks: %d" % (msg.left_ticks, msg.right_ticks))


if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node_subscriber')

    # keep spinning
    rospy.spin()
