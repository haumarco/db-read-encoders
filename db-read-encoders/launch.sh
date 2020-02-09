#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------


echo "Diagnostic: Current directory is" $PWD 
cd packages/pigpio-74
echo "Diagnostic: Changed directory to" $PWD "to install pigpio library"
make . &> /dev/null
sudo make install &> /dev/null
echo "Diagnostic: Installed successfully"
cd ../..
echo "Diagnostic: Returned to top-level directory" $PWD "to invoke pigpio library"
#sudo killall pigpiod # This just seems to fail then halts the process.
#echo "Diagnostic: Killing all previous instances of pigpio daemon" # Related to the line above.
sudo pigpiod


## Use ROSlaunch to run the encoder file
#roslaunch read_encoders encoder.launch

## This launches the encoder and its subscriber node
roslaunch read_encoders multiple_nodes.launch
#roslaunch read_encoders diagnostic_tests.launch
