include "Robots/Sensor.inc" 

define CarrierRobot position 
( 
  #properties as name value pairs
  size [1.8 1.5 0.5] 
  drive "diff" 
  block( #body
  	points 6 
  	point[0] [0 20]
    point[1] [100 20]
    point[2] [90 30]
    point[3] [90 70]
    point[4] [100 80]
    point[5] [0 80]
  	z [20 100]
  )

  block( #left wheel
    points 4
    point[0] [0 0]
    point[1] [100 0]
    point[2] [100 20]
    point[3] [0 20]
    z [0 40]
    color "dark slate gray"
  )

  block( #right wheel
    points 4
    point[0] [0 80]
    point[1] [100 80]
    point[2] [100 100]
    point[3] [0 100]
    z [0 40]
    color "dark slate gray"
  )
   
    Sensor(pose [0.9 0.75 -0.4 -20]) #left sensor
    Sensor(pose [0.9 -0.75 -0.4 20]) #right sensor
) 
