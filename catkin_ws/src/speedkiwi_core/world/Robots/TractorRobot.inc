include "Robots/Sensor.inc"

define TractorRobot position 
( 
  #properties as name value pairs
  size [4 3 2.3.0] 
  drive "diff" 

  block( # cab
  	points 4 
  	point[0] [.3 3] 
  	point[1] [.3 7] 
  	point[2] [3.9 7]
	  point[3] [3.9 3] 
  	z [2.5 10]
  )

  block( # body
    points 4 
    point[0] [3.9 3.5] 
    point[1] [3.9 6.5] 
    point[2] [10 6.5]
    point[3] [10 3.5] 
    z [2.5 7.5]
  )

  block( # left back tyre
    points 4 
    point[0] [0 0] 
    point[1] [0 3] 
    point[2] [4 3]
    point[3] [4 0] 
    z [0 5]
    color "black"
  )
  block( # left back wheel
    points 4 
    point[0] [1 -.1] 
    point[1] [1 3.1] 
    point[2] [3 3.1]
    point[3] [3 -.1] 
    z [1 4]
    color "yellow"
  )

  block( # right back tyre
    points 4 
    point[0] [0 7] 
    point[1] [0 10] 
    point[2] [4 10]
    point[3] [4 7] 
    z [0 5]
    color "black"
  )
  block( # right back wheel
    points 4 
    point[0] [1 6.9] 
    point[1] [1 10.1] 
    point[2] [3 10.1]
    point[3] [3 6.9] 
    z [1 4]
    color "yellow"
  )




  block( # left front tyre
    points 4 
    point[0] [7 6.5] 
    point[1] [7 8.5] 
    point[2] [10 8.5]
    point[3] [10 6.5] 
    z [0 4]
    color "black"
  )
  block( # left front wheel
    points 4 
    point[0] [7.6 6.4] 
    point[1] [7.6 8.6] 
    point[2] [9.4 8.6]
    point[3] [9.4 6.4] 
    z [1 3]
    color "yellow"
  )

  block( # right front tyre
    points 4 
    point[0] [7 1.5] 
    point[1] [7 3.5] 
    point[2] [10 3.5]
    point[3] [10 1.5] 
    z [0 4]
    color "black"
  )
  block( # right front wheel
    points 4 
    point[0] [7.6 1.4] 
    point[1] [7.6 3.6] 
    point[2] [9.4 3.6]
    point[3] [9.4 1.4] 
    z [1 3]
    color "yellow"
  )



    Sensor(pose [2 1.5 -1.4 -20]) #left sensor
    Sensor(pose [2 -1.5 -1.4 20]) #right sensor
) 
