define orchardWalls model
(
# Colouring the surrounding trees
color "dark green"

# Whether to draw a bounding box around the model, indicating its size
boundary 0

# Can you interact with with model with the mouse
gui_move 0

)

orchardWalls( 
  name "OrchardWalls"
  bitmap "Trees.png"
  size [ 46.0 95.0 5 ]
  pose [ 0.000 0.000 0 0 ]
)

