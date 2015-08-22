<<<<<<< HEAD
#define the sensor for the Picker robot
include "Robots/Sensor.inc"

define BinRobot position 
( 
  #properties as name value pairs
=======
define BinRobot position 
( 
  #properties as name value pairs

  #drive "diff"
>>>>>>> 0d18d252049456e0a840a6f99c25d1dfd6834d20
  size [1 1 1] 
  obstacle_return 0
  laser_return 0
  ranger_return 0
<<<<<<< HEAD
  drive "diff" 
=======

>>>>>>> 0d18d252049456e0a840a6f99c25d1dfd6834d20
  block(
  	points 4 
  	point[0] [0 0] 
  	point[1] [0 1.5] 
  	point[2] [2.5 1.5]
<<<<<<< HEAD
	point[3] [2.5 0] 
=======
	  point[3] [2.5 0] 
>>>>>>> 0d18d252049456e0a840a6f99c25d1dfd6834d20
  	z [0 1]
    )
) 
