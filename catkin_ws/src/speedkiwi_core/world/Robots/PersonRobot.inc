include "Robots/Sensor.inc"

define PersonRobot position 
( 
  #properties as name value pairs
  size [0.4 0.6 1.6] 
  drive "diff" 

  block( #right foot
    points 4
    point[0] [0.2 0.12]
    point[1] [0.2 0.22]
    point[2] [0.35 0.22]
    point[3] [0.35 0.12]
    z [0 0.1]
    color "black"
  )

  block( #left foot
    points 4
    point[0] [0.2 0.38]
    point[1] [0.2 0.48]
    point[2] [0.35 0.48]
    point[3] [0.35 0.38]
    z [0 0.1]
    color "black"
  )

  block( #head
    points 4
    point[0] [0.2 0.2]
    point[1] [0.2 0.4]
    point[2] [0.3 0.4]
    point[3] [0.3 0.2]
    z [1.4 1.6]
    color "PeachPuff1"
  )

  block( #left arm
    points 4
    point[0] [0.2 0]
    point[1] [0.2 0.1]
    point[2] [0.3 0.1]
    point[3] [0.3 0]
    z [0.75 1.35]
    color "PeachPuff1"
  )

  block( #right arm
    points 4
    point[0] [0.2 0.5]
    point[1] [0.2 0.6]
    point[2] [0.3 0.6]
    point[3] [0.3 0.5]
    z [0.75 1.35]
    color "PeachPuff1"
  )

  block( #right leg
    points 4 
    point[0] [0.2 0.12] 
    point[1] [0.2 0.22] 
    point[2] [0.3 0.22]
    point[3] [0.3 0.12] 
    z [0 0.8]
    color "DodgerBlue4"
  )

  block( #left leg
    points 4
    point[0] [0.2 0.38]
    point[1] [0.2 0.48]
    point[2] [0.3 0.48]
    point[3] [0.3 0.38]
    z [0 0.8]
    color "DodgerBlue4"
  )

  block( #torso
    points 4
    point[0] [0.2 0.1]
    point[1] [0.2 0.5]
    point[2] [0.3 0.5]
    point[3] [0.3 0.1]
    z [0.8 1.4]
    color "hot pink"
  )

  block( #hat base
    points 4
    point[0] [0.15 0.1]
    point[1] [0.15 0.5]
    point[2] [0.35 0.5]
    point[3] [0.35 0.1]
    z [1.6 1.63]
    color "saddle brown"
  )

  block( #hat top
    points 4
    point[0] [0.2 0.2]
    point[1] [0.2 0.4]
    point[2] [0.3 0.4]
    point[3] [0.3 0.2]
    z [1.63 1.7]
    color "saddle brown" 
  )

    Sensor(pose [0.2 0.3 -1.3 -20]) #left sensor
    Sensor(pose [0.2 -0.3 -1.3 20]) #right sensor
) 
