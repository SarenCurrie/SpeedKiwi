robotsDict = dict()

def addRobot(object, id):
	robotsDict[id] = object

def getRobotWithId(id):
	return robotsDict[id]

def get_robot_list():
	return robotsDict