#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------

# Installing the pigpio library.
# This runs each time the docker container is run, but 
# this process can be started just after booting the
# duckiebots.
echo "Install process for pigpio library"
echo "Diagnostic: Current directory is" $PWD 
cd packages/pigpio-74
echo "Diagnostic: Changed directory to" $PWD "to install pigpio library"
make . &> /dev/null
sudo make install &> /dev/null
echo "Diagnostic: Installed successfully"
cd ../..
echo "Diagnostic: Returned to top-level directory" $PWD "to invoke pigpio library"

#sudo killall pigpiod # This just seems to fail, then halts the process. --> Do not uncomment
#echo "Diagnostic: Killing all previous instances of pigpio daemon" # Related to the line above.


## If the pigpio daemon does not successfully launch, 
##	make sure that the docker run command is given the --privileged argument
##	try re-booting the duckiebot to clear the robot's cache memory
##	halt (Ctrl-C) extraneous processes running on the Duckiebot, such as gui_tools.
sudo pigpiod


## Use ROSlaunch to run the encoder file
roslaunch read_encoders encoder.launch

# This launches the encoder and its subscriber node
# The subscriber node acts as a diagnostic test to check that the encoders are publishing correctly.
# For diagnostic tests, please comment the following line for multiple_nodes.launch and uncomment diagnostic_tests.launch

#roslaunch read_encoders multiple_nodes.launch
#roslaunch read_encoders diagnostic_tests.launch
