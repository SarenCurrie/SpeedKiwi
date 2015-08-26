# Dictionary of all robots created.
# Used to gain access to other robots from other robots.

robotsDict = dict()


def addRobot(object, id):
	# Add robot to dictionary
    robotsDict[id] = object


def getRobotWithId(id):
	# Get robot in dictionary with specified id.
    return robotsDict[id]


def get_robot_list():
	# Return the dictionary of robots.
    return robotsDict
