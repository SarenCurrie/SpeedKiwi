# define newentity oldentity ()

#define the sensor for the Picker robot
define Sensor ranger 
( 
  sensor( range [ 0 3 ] fov 40.0 samples 500 ) 
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
    Sensor(pose [1.25 0.75 -0.75 -20]) #left sensor
    Sensor(pose [1.25 -0.75 -0.75 20]) #right sensor
    
) 
