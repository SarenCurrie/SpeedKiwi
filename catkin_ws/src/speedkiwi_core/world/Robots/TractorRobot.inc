include "Robots/Sensor.inc"

define TractorRobot position 
( 
  #properties as name value pairs
  size [4.5 3 2.3.0] 
  drive "diff" 
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
	point[3] [2.5 0] 
  	z [0 1]
    )
    Sensor(pose [2.25 1.5 -2 -20]) #left sensor
    Sensor(pose [2.25 -1.5 -2 20]) #right sensor
) 
