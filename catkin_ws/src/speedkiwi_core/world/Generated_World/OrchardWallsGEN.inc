define orchardWalls model
(
# Colouring the surrounding trees
color "dark green"

# Whether to draw a bounding box around the model, indicating its size
boundary 0

# Can you interact with with model with the mouse
gui_move 0

)

# Size of orchard walls is the width/length of the orchard + 30 (15m each size)
orchardWalls( 
  name "OrchardWalls"
  bitmap "Trees.png"
  size [ 51.0 100.0 2 ]
  pose [ 0.000 0.000 0 0 ]
)

