include "Robots/Sensor.inc"

define PickerRobot position 
( 
  #properties as name value pairs
  size [2.5 1.5 1.0] 
  drive "diff" 
  obstacle_return 1
  
  block( #body
    points 8
    point[0] [20 20]
    point[1] [0 35]
    point[2] [0 65]
    point[3] [20 80]
    point[4] [80 80]
    point[5] [100 65]
    point[6] [100 35]
    point[7] [80 20]
    z [10 50]
    color "orange"
  )

  block( #left track layer 1
  	points 4 
  	point[0] [10 0] 
  	point[1] [90 0] 
  	point[2] [90 20]
    point[3] [10 20] 
  	z [0 6]
    color "dark slate gray"
  )

  block( #left track layer 2
    points 4
    point[0] [0 0]
    point[1] [100 0]
    point[2] [100 20]
    point[3] [0 20]
    z [6 14]
    color "dark slate gray"
  )

  block( #left track layer 3
    points 4
    point[0] [10 0] 
    point[1] [90 0] 
    point[2] [90 20]
    point[3] [10 20]
    z [14 20]
    color "dark slate gray"
  )

  block( #right track layer 1
    points 4
    point[0] [10 80]
    point[1] [90 80]
    point[2] [90 100]
    point[3] [10 100]
    z [0 6]
    color "dark slate gray"
  )

  block( #right track layer 2
    points 4
    point[0] [0 80]
    point[1] [100 80]
    point[2] [100 100]
    point[3] [0 100]
    z [6 14]
    color "dark slate gray"
  )  

  block( #right track layer 3
    points 4
    point[0] [10 80]
    point[1] [90 80]
    point[2] [90 100]
    point[3] [10 100]
    z [14 20]
    color "dark slate gray"
  )

  Sensor(pose [1.25 0.75 -0.9 -20]) #left sensor
  Sensor(pose [1.25 -0.75 -0.9 20]) #right sensor
) 
