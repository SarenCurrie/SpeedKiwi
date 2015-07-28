cmake_minimum_required(VERSION 2.8.3)
project(test)

find_package(catkin REQUIRED COMPONENTS message_generation rospy)

# add_message_files(
#   FILES Floats.msg HeaderString.msg
# )
# add_service_files(
#   DIRECTORY srv
#   FILES AddTwoInts.srv BadTwoInts.srv
# )

## Generate services in the 'srv' folder
# add_service_files(
#  FILES  # e.g. Floats.srv HeaderString.srv
#)

## Generate added messages and services with any dependencies
# generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime
)

catkin_python_setup()

install(PROGRAMS bin/hello
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
