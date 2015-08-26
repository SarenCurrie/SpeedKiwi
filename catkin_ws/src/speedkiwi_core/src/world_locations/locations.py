import os

orchard_boundaries = dict()
wall_boundaries = dict()
bin_locations = dict()

# define max/min coordinates for orchard space
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "orchard_corners.txt", 'r') as file:
    data = file.readlines()

orchard_boundaries["max_x"] = float(data[2]) # max x
orchard_boundaries["max_y"] = float(data[4]) # max y
orchard_boundaries["min_x"] = float(data[6]) # min x
orchard_boundaries["min_y"] = float(data[8]) # min y
file.close()

# define tractor boundaries
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "wall_corners.txt", 'r') as file:
    data = file.readlines()
wall_boundaries["min_x"]  = float(data[2])
wall_boundaries["max_x"]  = float(data[4])
wall_boundaries["min_y"]  = float(data[6])
wall_boundaries["max_y"]  = float(data[8])
file.close()

# define bin locations
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "bin_locations.txt", 'r') as file:
    data = file.readlines()
bin_locations["max_x"]  = float(data[2])
bin_locations["max_y"]  = float(data[4])
bin_locations["min_x"]  = float(data[6])
bin_locations["min_y"]  = float(data[8])
file.close()

def get_bin_locations():
	return bin_locations

def get_orchard_boundaries():
	return orchard_boundaries

def get_wall_boundaries():
	return wall_boundaries


	