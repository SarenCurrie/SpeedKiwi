from robot import Robot
import rospy
import os

class PickerRobot(Robot):

    """Robot that picks kiwifruit and puts it in queue"""
    def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
        Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
        #Define orchard edge coordinates
        dir = os.path.dirname(__file__)
        path = os.path.join(dir,"world_locations/")
        with open(path + "orchard.txt", 'r') as file:
            #read orchard location file
            data = file.readlines()

        self.maxX = float(data[1]) 
        self.maxY = float(data[2])
        self.minX = float(data[3])
        self.minY = float(data[4])
        file.close()
        self.type = type(self).__name__

    def execute_callback(self):
        """docstring for execute_callback"""
        currentX = self.position['x']
        currentY = self.position['y']
        inOrchard = False #used for debugging purposes
        #check if in orchard area
        if ((self.minX <= currentX <= self.maxX) and (self.minY <= currentY <= self.maxY)):
            inOrchard = True
            self.do_picking()
            """need to slow down robot to 0.01m/s"""

    def do_picking(self):
        """Execute picking behaviour"""
        rospy.loginfo(self.robot_id + " is picking!")
