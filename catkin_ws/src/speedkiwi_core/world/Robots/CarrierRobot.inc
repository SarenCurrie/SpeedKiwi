include "Robots/Sensor.inc" 

define CarrierRobot position 
( 
  #properties as name value pairs
  size [1.8 1.5 0.5] 
  drive "diff" 
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
	point[3] [2.5 0] 
  	z [0 1]
    )
   
    Sensor(pose [0.9 0.75 -0.4 -20]) #left sensor
    Sensor(pose [0.9 -0.75 -0.4 20]) #right sensor
) 
