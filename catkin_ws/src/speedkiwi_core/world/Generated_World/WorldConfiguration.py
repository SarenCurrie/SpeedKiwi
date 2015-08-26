from xml.dom import minidom
import os

world_path = "src/speedkiwi_core/world/Generated_World/"
locations_path = "src/speedkiwi_core/src/world_locations/"

# Read the xml file and obtain the configured values.
xmldoc = minidom.parse(world_path + 'WorldVariables.xml')
configureList = xmldoc.getElementsByTagName('Configure')

treeHeight = configureList[0].firstChild.nodeValue
rowWidth = configureList[1].firstChild.nodeValue
rowNum = configureList[2].firstChild.nodeValue
colLength = configureList[3].firstChild.nodeValue
postSpacing = configureList[4].firstChild.nodeValue

# Calculate the remaining non-configurable values.
colNum = float(colLength) / float(postSpacing) + 1
rowLength = (float(rowNum) - 1) * float(rowWidth)

# Calculates the offsets so that the orchard is positioned in the center of the stage.
xOffSet = float(rowLength)/2
yOffSet = float(colLength)/2


# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
# |M|o|d|e|l| |p|o|s|i|t|i|o|n|s|
# +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+

# --------------- Pergola Post Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(world_path + "PergolaPostPositionsGEN.inc")):
    os.remove(world_path + "PergolaPostPositionsGEN.inc")

# Open the newly generated file.
postFile = open(world_path + "PergolaPostPositionsGEN.inc", "a")

# Prints all of the Pergola Posts code
for i in range(0, int(rowNum)):
    for j in range(0, int(colNum)):
        postFile.write("PergolaPost(\n")
        postFile.write("pose [ %.3f %.3f 0.000 0.000 ]\n" % (i*float(rowWidth) - xOffSet, float(colLength) - j*float(postSpacing) - yOffSet))
        postFile.write(")\n")

postFile.close()


# --------------- Pergola Arch Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(world_path + "PergolaArchPositionsGEN.inc")):
    os.remove(world_path + "PergolaArchPositionsGEN.inc")

# Open the newly generated file.
archFile = open(world_path + "PergolaArchPositionsGEN.inc", "a")

for i in range(0, int(rowNum) - 1):
    for j in range(0, int(colNum)):
        archFile.write("PergolaArch(\n")
        archFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) + float(rowWidth) / float(2) - xOffSet, float(colLength) - j*float(postSpacing) - yOffSet, float(treeHeight)))
        archFile.write(")\n")

        if (j != int(colNum) - 1):
            # Adding in more arches
            archFile.write("PergolaArch(\n")
            archFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) + float(rowWidth) / float(2) - xOffSet, float(colLength) - j*float(postSpacing) - float(postSpacing)*0.25 - yOffSet, float(treeHeight)))
            archFile.write(")\n")

            # Adding in more arches
            archFile.write("PergolaArch(\n")
            archFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) + float(rowWidth) / float(2) - xOffSet, float(colLength) - j*float(postSpacing) - float(postSpacing)*0.5 - yOffSet, float(treeHeight)))
            archFile.write(")\n")

            # Adding in more arches
            archFile.write("PergolaArch(\n")
            archFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) + float(rowWidth) / float(2) - xOffSet, float(colLength) - j*float(postSpacing) - float(postSpacing)*0.75 - yOffSet, float(treeHeight)))
            archFile.write(")\n")

archFile.close()


# --------------- Pergola Brace Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(world_path + "PergolaBracePositionsGEN.inc")):
    os.remove(world_path + "PergolaBracePositionsGEN.inc")

# Open the newly generated file.
braceFile = open(world_path + "PergolaBracePositionsGEN.inc", "a")

for i in range(0, int(rowNum)):
    braceFile.write("PergolaBrace(\n")
    braceFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) - xOffSet, float(colLength) / 2 - yOffSet, float(treeHeight)-float(0.3)))
    braceFile.write(")\n")

braceFile.close()


# Therefore the y pos of the road needs to be Length/6 - Length/2
# 16.67 - 50 = 33

# Therefore the x pos of the road needs to be Width/2 + Driveway/4
# 25.5 + 1.5


# --------------- Driveway Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(world_path + "DrivewayPositionGEN.inc")):
    os.remove(world_path + "DrivewayPositionGEN.inc")

# Open the newly generated file.
braceFile = open(world_path + "DrivewayPositionGEN.inc", "a")

braceFile.write("Driveway(\n")
# Positions the the driveway in the space at the bottom right
braceFile.write("pose [ %.3f %.3f 0.000 0.000 ]\n" % ((float(rowLength)+50)/2 + 3, (float(colLength)+50)/6 - (float(colLength)+50)/2 ))
braceFile.write(")\n")

braceFile.close()


# +-+-+-+-+-+ +-+-+-+-+-+
# |M|o|d|e|l| |s|i|z|e|s|
# +-+-+-+-+-+ +-+-+-+-+-+

# --------------- Change the Pergola Arch Model size --------------- #
# Read the file
with open(world_path + "PergolaArchGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [0.3 %.1f 0.4]\n' % float(rowWidth)
# Write to the file
with open(world_path + "PergolaArchGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Pergola Post Model size --------------- #
# Read the file
with open(world_path + "PergolaPostGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [ 0.3 0.3 %.1f ]\n' % float(treeHeight)
# Write to the file
with open(world_path + "PergolaPostGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Pergola Brace Model size --------------- #
# Read the file
with open(world_path + "PergolaBraceGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [ %.1f 0.3 0.3 ]\n' % float(colLength)
# Write to the file
with open(world_path + "PergolaBraceGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Orchard Wall size --------------- #
# Read the file
with open(world_path + "OrchardWallsGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()
# Make the pergola walls 25m on each side bigger then the orchard
data[17] = '  size [ %.1f %.1f 3 ]\n' % (float(rowLength)+float(50), float(colLength)+float(50))
# Write to the file
with open(world_path + "OrchardWallsGEN.inc", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Change the Driveway Model size --------------- #
# Read the file
with open(world_path + "DrivewayGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [12 %.1f 0.01]\n' % ((float(colLength)+float(50))/3)
# Write to the file
with open(world_path + "DrivewayGEN.inc", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Change the Floormap Model size --------------- #
# Read the file
with open(world_path + "FloormapGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [%.1f %.1f 0.001]\n' % (float(rowLength)+70, float(colLength)+70)
# Write to the file
with open(world_path + "FloormapGEN.inc", 'w') as file:
    file.writelines(data)

file.close()



 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 #|P|o|i|n|t| |L|o|c|a|t|i|o|n|s|
 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+


# --------------- Generate world wall corner points --------------- #
# Read the file
with open(locations_path + "wall_corners.txt", 'r') as file:
    # Read the location file
    data = file.readlines()

data[2] = "%.1f\n" % (-xOffSet-22)
data[4] = "%.1f\n" % (xOffSet+22)
data[6] = "%.1f\n" % (-yOffSet-22)
data[8] = "%.1f\n" % (yOffSet+22)

# Write to the file
with open(locations_path + "wall_corners.txt", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Generate world orchard corner points --------------- #
# Read the file
with open(locations_path + "orchard_corners.txt", 'r') as file:
    # Read the location file
    data = file.readlines()

data[2] = "%.1f\n" % (xOffSet)
data[4] = "%.1f\n" % (yOffSet)
data[6] = "%.1f\n" % (-xOffSet)
data[8] = "%.1f\n" % (-yOffSet)

# Write to the file
with open(locations_path + "orchard_corners.txt", 'w') as file:
    file.writelines(data)

file.close()



# --------------- Set configured robot positions in main() --------------- #

# Read the file
with open("src/speedkiwi_core/src/main.py", 'r') as file:
    # Read the main file
    data = file.readlines()
    data[13] = "animal = Animal('robot_0', 2, 0.5, %.1f, 0, 0)\n" % (xOffSet+10)

    data[15] = "person1 = Person('robot_1', 2, 0.5, 0, %.1f, 0)\n" % (yOffSet+10)
    data[16] = "person2 = EducatedPerson('robot_2', 2, 0.5, %.1f, 0, 0)\n" % (-xOffSet-10)

    data[18] = "tractor = Tractor('robot_3', 2, 0.9, %.1f, %.1f, 0)\n" % (-xOffSet-25+10, yOffSet+25-10)

    data[20] = "binbot1 = Bin('robot_4', 3, 0.5, %.1f, %.1f, pi/2)\n" % (0.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[21] = "binbot2 = Bin('robot_5', 3, 0.5, %.1f, %.1f, pi/2)\n" % (1.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[22] = "binbot3 = Bin('robot_6', 3, 0.5, %.1f, %.1f, pi/2)\n" % (2.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[23] = "binbot4 = Bin('robot_7', 3, 0.5, %.1f, %.1f, pi/2)\n" % (3.5*float(rowWidth)-xOffSet,-yOffSet-4)

    data[25] = "picker1 = PickerRobot('robot_8', 3, 0.5, %.1f, %.1f, 0)\n" % (0.5*float(rowWidth)-xOffSet,-yOffSet-9)
    data[26] = "picker2 = PickerRobot('robot_9', 3, 0.5, %.1f, %.1f, 0)\n" % (2.6*float(rowWidth)-xOffSet,-yOffSet-9)
    data[27] = "picker3 = PickerRobot('robot_10', 3, 0.5, %.1f, %.1f, 0)\n" % (4.7*float(rowWidth)-xOffSet,-yOffSet-9)

    data[29] = "carrier1 = CarrierRobot('robot_11', 3, 0.5, %.1f, %.1f, 0)\n" % ((float(rowLength) + 50)/2,(float(colLength)+50)/6-(float(colLength)+50)/2-0.75*(float(colLength)+50)/3)
    data[30] = "carrier2 = CarrierRobot('robot_12', 2, 0.5, %.1f, %.1f, 0)\n" % ((float(rowLength) + 50)/2+6,(float(colLength)+50)/6-(float(colLength)+50)/2-0.25*(float(colLength)+50)/3)

    # Write to the file
with open("src/speedkiwi_core/src/main.py", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Set configured robot positions in RobotListGEN --------------- #

# Read the file
with open("src/speedkiwi_core/world/Robots/RobotListGEN.inc", 'r') as file:
    # Read the main file
    data = file.readlines()

    data[1] = "AnimalRobot( pose [ %.1f 0.000 0.000 0.000 ] name \"animal\" color \"yellow\")\n" % (xOffSet+10)

    data[3] = "PersonRobot( pose [ 0.000 %.1f 0.000 0.000 ] name \"uneducatedPerson\")\n" % (yOffSet+10)
    data[4] = "PersonRobot( pose [ %.1f 0.000 0.000 0.000 ] name \"educatedPerson\")\n" % (-xOffSet-10)

    data[6] = "TractorRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"tractorRobot\")\n" % (-xOffSet-25+10, yOffSet+25-10)

    data[8] = "BinRobot( pose [ %.1f %.1f 0.150 90.000 ] name \"bin1\")\n" % (0.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[9] = "BinRobot( pose [ %.1f %.1f 0.150 90.000 ] name \"bin2\")\n" % (1.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[10] = "BinRobot( pose [ %.1f %.1f 0.150 90.000 ] name \"bin3\")\n" % (2.5*float(rowWidth)-xOffSet,-yOffSet-4)
    data[11] = "BinRobot( pose [ %.1f %.1f 0.150 90.000 ] name \"bin4\")\n" % (3.5*float(rowWidth)-xOffSet,-yOffSet-4)

    data[13] = "PickerRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"pickerRobot1\")\n" % (0.5*float(rowWidth)-xOffSet,-yOffSet-9)
    data[14] = "PickerRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"pickerRobot2\")\n" % (2.6*float(rowWidth)-xOffSet,-yOffSet-9)
    data[15] = "PickerRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"pickerRobot3\")\n" % (4.7*float(rowWidth)-xOffSet,-yOffSet-9)

    data[17] = "CarrierRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"carrierRobot1\")\n" % ((float(rowLength) + 50)/2,(float(colLength)+50)/6-(float(colLength)+50)/2 + 0.375*(float(colLength)+50)/3)
    data[18] = "CarrierRobot( pose [ %.1f %.1f 0.000 0.000 ] name \"carrierRobot2\")\n" % ((float(rowLength) + 50)/2+6,(float(colLength)+50)/6-(float(colLength)+50)/2 + 0.125*(float(colLength)+50)/3)

        # Write to the file
with open("src/speedkiwi_core/world/Robots/RobotListGEN.inc", 'w') as file:
    file.writelines(data)

file.close()