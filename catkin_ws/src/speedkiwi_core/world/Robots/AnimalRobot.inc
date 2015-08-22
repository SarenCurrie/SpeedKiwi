#define the sensor for the Picker robot
include "Robots/Sensor.inc"

define AnimalRobot position 
( 
  #properties as name value pairs
  size [1.5 0.5 0.9] 
  drive "diff" 
  block( #back right leg
    points 4 
  	point[0] [0 0] 
  	point[1] [0 0.1] 
  	point[2] [0.1 0.1]
    point[3] [0.1 0] 
  	z [0 0.4]
  )
  block( #back left leg
    points 4
    point[0] [0.4 0]
    point[1] [0.5 0]
    point[2] [0.5 0.1]
    point[3] [0.4 0.1]
    z [0 0.4]
  )
  block( #front right leg
    points 4
    point[0] [0 0.4]
    point[1] [0 0.5]
    point[2] [0.1 0.5]
    point[3] [0.1 0.4]
    z [0 0.4]
  )
  block( #front left leg
    points 4
    point[0] [0.5 0.4]
    point[1] [0.5 0.5]
    point[2] [0.4 0.5]
    point[3] [0.4 0.4]
    z [0 0.4]
  )
  block( #front left leg
    points 4
    point[0] [0.5 0.4]
    point[1] [0.5 0.5]
    point[2] [0.4 0.5]
    point[3] [0.4 0.4]
    z [0 0.4]
  )

  block( #body
    points 4
    point[0] [0 0]
    point[1] [0 0.5]
    point[2] [0.5 0.5]
    point[3] [0.5 0]
    z [0.4 0.7]
  )

  block( #head
    points 4
    point[0] [0.5 0.1]
    point[1] [0.5 0.4]
    point[2] [0.8 0.4]
    point[3] [0.8 0.1]
    z [0.6 0.9]
  )

  block( #left eye
    points 4
    point[0] [0.8 0.13]
    point[1] [0.8 0.20]
    point[2] [0.81 0.20]
    point[3] [0.81 0.13]
    z [0.82 0.85]
    color "black"
  )

  block( #right eye
    points 4
    point[0] [0.8 0.30]
    point[1] [0.8 0.37]
    point[2] [0.81 0.37]
    point[3] [0.81 0.30]
    z [0.82 0.85]
    color "black"
  )

  block( #left ear
    points 4
    point[0] [0.6 0.1]
    point[1] [0.7 0.1]
    point[2] [0.7 0.08]
    point[3] [0.6 0.08]
    z [0.5 0.9]
  )

  block( #right ear
    points 4
    point[0] [0.6 0.4]
    point[1] [0.6 0.42]
    point[2] [0.7 0.42]
    point[3] [0.7 0.4]
    z [0.5 0.9]
  )

  block( #tail
    points 4
    point[0] [0 0.2]
    point[1] [0 0.3]
    point[2] [-0.2 0.3]
    point[3] [-0.2 0.2]
    z [0.65 0.7]
  )

    Sensor(pose [0.75 0.15 -0.1 -20]) #left sensor
    Sensor(pose [0.75 -0.15 -0.1 20]) #right sensor
)