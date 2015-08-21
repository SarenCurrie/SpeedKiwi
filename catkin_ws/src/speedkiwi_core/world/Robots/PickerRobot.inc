include "Robots/Sensor.inc"

define PickerRobot position 
( 
  #properties as name value pairs
  size [2.5 1.5 1.0] 
  drive "diff" 
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
	point[3] [2.5 0] 
  	z [0 1]
    )
    Sensor(pose [1.25 0 -0.75 0])
) 
