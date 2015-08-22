define Sensor ranger 
( 
  sensor( range [ 0 3 ] fov 40.0 samples 500 ) 
  size [0.01 0.01 0.01] 
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
