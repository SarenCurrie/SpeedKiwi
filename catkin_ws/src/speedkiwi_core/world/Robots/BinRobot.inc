#define the sensor for the Picker robot
include "Robots/Sensor.inc"

define BinRobot position 
( 
  #properties as name value pairs
  size [1 1 1] 
  drive "diff" 
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
	point[3] [2.5 0] 
  	z [0 1]
    )
) 
