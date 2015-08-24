from xml.dom import minidom
import os

locations_path = "src/speedkiwi_core/src/world_locations/"

 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 #|P|o|i|n|t| |L|o|c|a|t|i|o|n|s|
 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+


# --------------- Generate world wall corner points --------------- #
# Read the file
with open(locations_path + "wall_corners.txt", 'r') as file:
    # Read the location file
    data = file.readlines()
    data[2] = "-35\n"
    data[4] = "35\n"
    data[6] = "-60\n"
    data[8] = "60\n"

# Write to the file
with open(locations_path + "wall_corners.txt", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Generate world orchard corner points --------------- #
# Read the file
with open(locations_path + "orchard_corners.txt", 'r') as file:
    # Read the location file
    data = file.readlines()
    data[2] = "10.5\n"
    data[4] = "35\n"
    data[6] = "-10.5\n"
    data[8] = "-35\n"

# Write to the file
with open(locations_path + "orchard_corners.txt", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Set default robot positions in main() --------------- #

# Read the file
with open("src/speedkiwi_core/src/main.py", 'r') as file:
    # Read the main file
    data = file.readlines()
    data[13] = "animal = Animal('robot_0', 2, 0.5, 19, -45, 0)\n"

    data[15] = "person1 = Person('robot_1', 2, 0.5, 0, 40, 0)\n"
    data[16] = "person2 = EducatedPerson('robot_2', 2, 0.5, 27, -48, 0)\n"

    data[18] = "tractor = Tractor('robot_3', 2, 0.9, -20, 43, 0)\n"

    data[20] = "binbot1 = Bin('robot_4', 3, 0.5, -8.75, -38, pi/2)\n"
    data[21] = "binbot2 = Bin('robot_5', 3, 0.5, -1.75, -38, pi/2)\n"
    data[22] = "binbot3 = Bin('robot_6', 3, 0.5, 1.75, -38, pi/2)\n"
    data[23] = "binbot4 = Bin('robot_7', 3, 0.5, 8.75, -38, pi/2)\n"

    data[25] = "picker1 = PickerRobot('robot_8', 3, 0.5, -8.75, -41, 0)\n"
    data[26] = "picker2 = PickerRobot('robot_9', 3, 0.5, 1, -41, 0)\n"
    data[27] = "picker3 = PickerRobot('robot_10', 3, 0.5, 5, -43, 0)\n"

    data[29] = "robot = Robot('robot_11', 3, 0.5, -8.5, -37, 0)  # Will be carrier #1\n"
    data[30] = "robot1 = DifferentRobot('robot_12', 2, 0.5, 0, 0, 0)  # Will be carrier #2\n"

    # Write to the file
with open("src/speedkiwi_core/src/main.py", 'w') as file:
    file.writelines(data)

file.close()