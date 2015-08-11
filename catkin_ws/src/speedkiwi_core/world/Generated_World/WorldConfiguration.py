from xml.dom import minidom
import os

path = "src/speedkiwi_core/world/Generated_World/"

# Read the xml file and obtain the configured values.
xmldoc = minidom.parse(path + 'WorldVariables.xml')
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


# --------------- Pergola Post Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(path + "PergolaPostPositionsGEN.inc")):
    os.remove(path + "PergolaPostPositionsGEN.inc")

# Open the newly generated file.
postFile = open(path + "PergolaPostPositionsGEN.inc", "a")

# Prints all of the Pergola Posts code
for i in range(0, int(rowNum)):
    for j in range(0, int(colNum)):
        postFile.write("PergolaPost(\n")
        postFile.write("pose [ %.3f %.3f 0.000 0.000 ]\n" % (i*float(rowWidth) - xOffSet, float(colLength) - j*float(postSpacing) - yOffSet))
        postFile.write(")\n")

postFile.close()


# --------------- Pergola Arch Position Generation --------------- #
# Check to make sure the file exists before deleting the previously generated file.
if (os.path.isfile(path + "PergolaArchPositionsGEN.inc")):
    os.remove(path + "PergolaArchPositionsGEN.inc")

# Open the newly generated file.
archFile = open(path + "PergolaArchPositionsGEN.inc", "a")

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
if (os.path.isfile(path + "PergolaBracePositionsGEN.inc")):
    os.remove(path + "PergolaBracePositionsGEN.inc")

# Open the newly generated file.
braceFile = open(path + "PergolaBracePositionsGEN.inc", "a")

for i in range(0, int(rowNum)):
    braceFile.write("PergolaBrace(\n")
    braceFile.write("pose [ %.3f %.3f %.3f 90.000 ]\n" % (i*float(rowWidth) - xOffSet, float(colLength) / 2 - yOffSet, float(treeHeight)-float(0.3)))
    braceFile.write(")\n")

braceFile.close()

# --------------- Change the Pergola Arch Model size --------------- #
# Read the file
with open(path + "PergolaArchGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [0.3 %.1f 0.4]\n' % float(rowWidth)
# Write to the file
with open(path + "PergolaArchGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Pergola Post Model size --------------- #
# Read the file
with open(path + "PergolaPostGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [ 0.3 0.3 %.1f ]\n' % float(treeHeight)
# Write to the file
with open(path + "PergolaPostGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Pergola Brace Model size --------------- #
# Read the file
with open(path + "PergolaBraceGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[2] = '  size [ %.1f 0.3 0.3 ]\n' % float(colLength)
# Write to the file
with open(path + "PergolaBraceGEN.inc", 'w') as file:
    file.writelines(data)

file.close()

# --------------- Change the Orchard Wall size --------------- #
# Read the file
with open(path + "OrchardWallsGEN.inc", 'r') as file:
    # Read the model file
    data = file.readlines()

data[16] = '  size [ %.1f %.1f 5 ]\n' % (float(rowLength)+float(25), float(colLength)+float(25))
# Write to the file
with open(path + "OrchardWallsGEN.inc", 'w') as file:
    file.writelines(data)

file.close()
