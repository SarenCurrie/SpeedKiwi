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

# --------------- Generate bin points --------------- #
# Read the file
with open(locations_path + "bin_locations.txt", 'r') as file:
    # Read the location file
    data = file.readlines()
    data[2] = "41.5\n"
    data[4] = "-45\n"
    data[6] = "35.5\n"
    data[8] = "-55\n"

# Write to the file
with open(locations_path + "bin_locations.txt", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Set default robot positions in main() --------------- #

# Read the file
with open("src/speedkiwi_core/src/main.py", 'r') as file:
    # Read the main file
    data = file.readlines()
    data[13] = "animal = Animal('robot_0', 2, 0.5, 20.5, 0, 0)\n"

    data[15] = "person1 = Person('robot_1', 2, 0.5, 0, 45, 0)\n"
    data[16] = "person2 = EducatedPerson('robot_2', 2, 0.5, -20.5, 0, 0)\n"

    data[18] = "tractor = Tractor('robot_3', 2, 0.9, -20.5, 45, 0)\n"

    data[20] = "binbot1 = Bin('robot_4', 3, 0.5, -8.75, -39, pi/2)\n"
    data[21] = "binbot2 = Bin('robot_5', 3, 0.5, -1.75, -39, pi/2)\n"
    data[22] = "binbot3 = Bin('robot_6', 3, 0.5, 1.75, -39, pi/2)\n"
    data[23] = "binbot4 = Bin('robot_7', 3, 0.5, 5.25, -39, pi/2)\n"

    data[25] = "picker1 = PickerRobot('robot_8', 3, 0.5, -8.75, -44, 0)\n"
    data[26] = "picker2 = PickerRobot('robot_9', 3, 0.5, 1, -44, 0)\n"
    data[27] = "picker3 = PickerRobot('robot_10', 3, 0.5, 7, -44, 0)\n"

    data[29] = "carrier1 = CarrierRobot('robot_11', 3, 0.5, 35.5, -25, 0)\n"
    data[30] = "carrier2 = CarrierRobot('robot_12', 2, 0.5, 41.5, -35, 0)\n"

    # Write to the file
with open("src/speedkiwi_core/src/main.py", 'w') as file:
    file.writelines(data)

file.close()















