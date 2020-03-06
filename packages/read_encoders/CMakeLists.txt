cmake_minimum_required(VERSION 2.8.3)
project(read_encoders)

find_package(catkin REQUIRED COMPONENTS
  rospy
  #marco
  duckietown_msgs # Every duckietown packages should use this.

# Only the encoder_ticks_node needs these
  std_msgs
  message_generation
)

add_message_files(
  FILES
  encoderTicksStamped.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
  message_runtime
)



### Original CMakeLists.txt file provided by https://docs.duckietown.org/daffy/duckietown-robotics-development/out/dt_infrastructure.html
#cmake_minimum_required(VERSION 2.8.3)
#project(my_package)
#
#find_package(catkin REQUIRED COMPONENTS
#  rospy
#)
#
#catkin_package()
