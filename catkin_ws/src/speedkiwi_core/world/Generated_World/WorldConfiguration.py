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
braceFile.write("pose [ %.3f %.3f 0.000 0.000 ]\n" % ((float(rowLength)+30)/2 + 1.5, (float(colLength)+30)/6 - (float(colLength)+30)/2 ))
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
# Make the pergola walls 15m on each side bigger then the orchard
data[17] = '  size [ %.1f %.1f 3 ]\n' % (float(rowLength)+float(30), float(colLength)+float(30))
# Write to the file
with open(world_path + "OrchardWallsGEN.inc", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Change the Driveway Model size --------------- #
# Read the file
with open(world_path + "DrivewayGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [6 %.1f 0.01]\n' % ((float(colLength)+float(30))/3)
# Write to the file
with open(world_path + "DrivewayGEN.inc", 'w') as file:
    file.writelines(data)

file.close()


# --------------- Change the Floormap Model size --------------- #
# Read the file
with open(world_path + "FloormapGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [%.1f %.1f 0.001]\n' % (float(rowLength)+50, float(colLength)+50)
# Write to the file
with open(world_path + "FloormapGEN.inc", 'w') as file:
    file.writelines(data)

file.close()



 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 #|P|o|i|n|t| |L|o|c|a|t|i|o|n|s|
 #+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+


# Generate world wall corner points




# Generate world orchard corner points
