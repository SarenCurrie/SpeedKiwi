define Floormap model
(
  size [90 140 0.001]
  obstacle_return 0
  gui_move 0

  block
  (
    color "medium sea green"
    points [4]
    point[0] [0 0]
    point[1] [0 1]
    point[2] [1 1]
    point[3] [1 0]
    z [0 0.1]
  )
)

Floormap(
  pose [0.000 0.000 0.000 0.000]
)
