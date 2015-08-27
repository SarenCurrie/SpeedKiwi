#!/bin/bash

# Sources ROS
source devel/setup.bash

if [[ $1 =~ ^[Dd]$ ]]; then
	python src/speedkiwi_core/world/Default_World/WorldConfiguration.py
	roslaunch speedkiwi_core DefaultLaunch.launch
	break;
elif [[ $1 =~ ^[Cc]$ ]]; then
	python src/speedkiwi_core/world/Generated_World/WorldConfiguration.py
	roslaunch speedkiwi_core GeneratedLaunch.launch
	break;
elif [[ $1 =~ ^[Tt]$ ]]; then
	python src/speedkiwi_core/world/Default_World/WorldConfiguration.py
	rostest speedkiwi_test TestLaunch.launch
	break;
fi





