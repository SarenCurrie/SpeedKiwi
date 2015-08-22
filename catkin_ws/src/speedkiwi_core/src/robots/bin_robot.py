# from robots import Robot
# import rospy

# class Bin(Robot):
#     """Robot that picks kiwifruit and puts it in queue"""
#     def __init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset):
#         Robot.__init__(self, robot_id, top_speed, angular_top_speed, x_offset, y_offset, theta_offset)
#         self.type = type(self).__name__
#         self.master = None

#     def latch(self, robot):
#         self.master = robot
#         #int(robot_id[-1:])
#         # rospy.loginfo(str(self.master))
#         # print str(self.master)


#     def mimic(self):
#         self.add_action(self.master.current_action())


#     def execute_callback(self):
#         """docstring for execute_callback"""
