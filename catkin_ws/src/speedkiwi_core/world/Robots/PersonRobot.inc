include "Robots/Sensor.inc"

define PersonRobot position 
( 
  #properties as name value pairs
  size [0.4 0.6 1.6] 
  drive "diff" 
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
	point[3] [2.5 0] 
  	z [0 1]
    )
    Sensor(pose [0.2 0.3 -1.3 -20]) #left sensor
    Sensor(pose [0.2 -0.3 -1.3 20]) #right sensor
) 
