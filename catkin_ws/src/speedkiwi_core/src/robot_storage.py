robotsDict = dict()

def addRobot(object, id):
	robotsDict[id] = object

def getRobotWithId(id):
	return robotsDict[id]