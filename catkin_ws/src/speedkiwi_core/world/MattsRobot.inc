# define newentity oldentity ()

#define the sensor for the Picker robot
define myLaser ranger 
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

define MattsRobot position 
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
    
    block( # right eye
    points 4 
    point[0] [2 .2] 
    point[1] [2 .7] 
    point[2] [2.51 .7]
    point[3] [2.51 .2] 
    z [.4 .85]
    color "white" 
    )
    block( # left eye
    points 4 
    point[0] [2 .8] 
    point[1] [2 1.3] 
    point[2] [2.51 1.3]
    point[3] [2.51 .8] 
    z [.4 .85]
    color "white" 
    )
    myLaser(pose [1.25 0 -0.75 0])
) 

