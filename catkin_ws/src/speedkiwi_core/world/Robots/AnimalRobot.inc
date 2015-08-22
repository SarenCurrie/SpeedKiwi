#define the sensor for the Picker robot
include "Robots/Sensor.inc"

define AnimalRobot position 
( 
  #properties as name value pairs
  size [0.9 0.5 0.5] 
  drive "diff" 
  block(
    points 4 
  	point[0] [0 0] 
  	point[1] [0 0.3] 
  	point[2] [0.3 0.3]
    point[3] [0.3 0] 
  	z [0 0.5]
    )
  block(
    points 4
    point[0] [0.8 0]
    point[1] [1.1 0]
    point[2] [1.1 0.3]
    point[3] [0.8 0.3]
    z [0 0.5]
  )
  block(
    points 4
    point[0] [0 0.8]
    point[1] [0 1.1]
    point[2] [0.3 1.1]
    point[3] [0.3 0.8]
    z [0 0.5]
  )

  block(
    points 4
    point[0] [0.8 0.8]
    point[1] [0.8 1.1]
    point[2] [1.1 1.1]
    point[3] [1.1 0.8]
    z [0 0.5]
  )

  block(
    points[0] [0 0]
    points[1] [0 1.1]
    points[2] [1.1 1.1]
    points[3] [1.1 0]
    z [0.5 0.8]
  )
    Sensor(pose [0.45 0.25 -0.4 -20]) #left sensor
    Sensor(pose [0.45 -0.25 -0.4 20]) #right sensor
) 
