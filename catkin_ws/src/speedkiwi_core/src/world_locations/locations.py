import os

orchard_boundaries = dict()
tractor_boundaries = dict()
row_locations = []

# define max/min coordinates for orchard space
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "orchard.txt", 'r') as file:
    data = file.readlines()

orchard_boundaries["max_x"] = float(data[1]) # max x
orchard_boundaries["max_y"] = float(data[2]) # max y
orchard_boundaries["min_x"] = float(data[3]) # min x
orchard_boundaries["min_y"] = float(data[4]) # min y
file.close()

# define row locations
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "row_locations.txt", 'r') as file:
    data = file.readlines()

row_locations.append(float(data[0])) 
row_locations.append(float(data[1])) 
row_locations.append(float(data[2]))
row_locations.append(float(data[3]))
row_locations.append(float(data[4]))
row_locations.append(float(data[5])) 
file.close()

# define tractor boundaries
dir = os.path.dirname(__file__)
path = os.path.join(dir,"../world_locations/")
with open(path + "tractor_boundaries.txt", 'r') as file:
    data = file.readlines()
tractor_boundaries["min_x"]  = int(data[2])
tractor_boundaries["max_x"]  = int(data[4])
tractor_boundaries["min_y"]  = int(data[6])
tractor_boundaries["max_y"]  = int(data[8])
file.close()

def get_orchard_boundaries():
	return orchard_boundaries

def get_row_locations():
	return row_locations

def get_tractor_boundaries():
	return tractor_boundaries


	