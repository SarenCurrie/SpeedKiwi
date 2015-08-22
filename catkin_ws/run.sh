#!/bin/bash

# Sources ROS
source devel/setup.bash

echo "Welcome Human!"
echo "Please select whether you want to create a:"
echo "- (D)efault environment"
echo "- (C)onfigured environment"
echo "OR"
echo "- run (T)ests"

while true;
do
read -p "Select and press Enter: " REPLY

if [[ $REPLY =~ ^[Dd]$ ]]; then
	roslaunch speedkiwi_core DefaultLaunch.launch	
	break;
	
elif [[ $REPLY =~ ^[Cc]$ ]]; then
	python src/speedkiwi_core/world/Generated_World/WorldConfiguration.py
	roslaunch speedkiwi_core GeneratedLaunch.launch
	break;
elif [[ $REPLY =~ ^[Tt]$ ]]; then
	chmod +x src/speedkiwi_test/src/test_move_action.py
	chmod +x src/speedkiwi_test/src/test_navigate_action.py
	chmod +x src/speedkiwi_test/src/test_robot.py
	rostest speedkiwi_test TestLaunch.launch

	break;
fi
done




