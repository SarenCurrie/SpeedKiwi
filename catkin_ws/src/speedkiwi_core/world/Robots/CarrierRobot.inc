#define the sensor for the Picker robot
define Sensor ranger 
( 
  sensor( range [ 0 4 ] fov 60.0 samples 500 ) 
  size [0.1 0.1 0.1] 
  color "black" 
  block( 
  points 4 
  point[0] [0 0] 
  point[1] [0.1 0] 
  point[2] [0.1 0.1] 
  point[3] [0 0.1] 
  z [0 0.1] 
  ) 
) 

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
    Sensor(pose [0.9 0 -0.4 0])
) 
