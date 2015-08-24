#define the sensor for the Picker robot
include "Robots/Sensor.inc"

define BinRobot position
( 
  #properties as name value pairs

  #drive "diff"
  size [1 1 1] 
  obstacle_return 0
  laser_return 0
  ranger_return 0

  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 10] 
  	point[2] [100 10]
	  point[3] [100 0] 
  	z [0 1]
    color "saddle brown"
  )

  block(
    points 4
    point[0] [0 10]
    point[1] [0 100]
    point[2] [10 100]
    point[3] [10 10]
    z [0 1]
    color "sienna"
  ) 

  block(
    points 4
    point[0] [10 100]
    point[1] [100 100]
    point[2] [100 90]
    point[3] [10 90]
    z [0 1]
    color "peru"
  )

  block(
    points 4
    point[0] [90 10]
    point[1] [90 90]
    point[2] [100 90]
    point[3] [100 10]
    z [0 1]
    color "sienna"
  )

  block( #bin bottom
    points 4
    point[0] [0 0]
    point[1] [0 100]
    point[2] [100 100]
    point[3] [100 0]
    z [0 0.01]
  )
) 
