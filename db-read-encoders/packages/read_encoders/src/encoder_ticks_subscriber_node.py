#!/usr/bin/env python

#### Needs work #########

import os
import rospy
from duckietown import DTROS
from std_msgs.msg import Header, Int32
from read_encoders.msg import encoderTicksStamped

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name)
        # construct publisher
        self.sub = rospy.Subscriber("encoder_ticks", encoderTicksStamped, self.cbPrint)
	#rospy.spin()
	rospy.loginfo("%s has started!" % node_name)

    def cbPrint(self, msg):
        #rospy.loginfo("I heard something:" )
	rospy.loginfo("Sub: Left ticks: %d \t Right ticks: %d" % (msg.left_ticks, msg.right_ticks))

#    def run(self):
#	rospy.loginfo("Margaritas")
#	while not rospy.is_shutdown():
#            # Not sure what to put here

if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node_subscriber')

#    # Default operation
#    node.run()

    # keep spinning
    rospy.spin()
