define PergolaArch model
(
  size [0.3 3.5 0.4]
  obstacle_return 0
  gui_move 0

  # Right most block
  block
  (
    color "chartreuse3"
    points [4]
    point[0] [0 0]
    point[1] [0 0.5]
    point[2] [0.5 0.5]
    point[3] [0.5 0]
    z [0 0.5]
  )
  # Right of middle block
  block
  (
    color "green3"
    points [4]
    point[0] [0 0.4]
    point[1] [0 1.25]
    point[2] [0.5 1.25]
    point[3] [0.5 0.4]
    z [0.5 1]
  )
  # Center block
  block
  (
    color "green4"
    points [4]
    point[0] [0 1.15]
    point[1] [0 2.35]
    point[2] [0.5 2.35]
    point[3] [0.5 1.15]
    z [1 1.5]
  )
  # Left of middle block
  block
 (
    color "green3"
    points [4]
    point[0] [0 2.25]
    point[1] [0 3.1]
    point[2] [0.5 3.1]
    point[3] [0.5 2.25]
    z [0.5 1]
  )
  # Left most block
  block
  (
     color "chartreuse3"
     points [4]
     point[0] [0 3]
     point[1] [0 3.5]
     point[2] [0.5 3.5]
     point[3] [0.5 3]
     z [0 0.5]
  )
)
