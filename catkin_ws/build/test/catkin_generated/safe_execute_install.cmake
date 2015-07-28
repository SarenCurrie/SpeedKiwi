execute_process(COMMAND "/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/build/test/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/Users/Saren/Documents/Uni/306/SpeedKiwi/catkin_ws/build/test/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
