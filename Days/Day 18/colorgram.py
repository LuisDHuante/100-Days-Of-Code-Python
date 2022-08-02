pip install colorgram.py

import colorgram

rgb_colors = []

# Extract 6 colors from an image.
colors = colorgram.extract('/flumequine.jpg', 30)
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r, g, b)
  rgb_colors.append(new_color)

print(rgb_colors)



colors = [(210, 149, 87), 
          (33, 98, 150), 
          (210, 211, 109), 
          (129, 171, 202), 
          (159, 58, 87), 
          (169, 73, 41), 
          (59, 123, 63), 
          (209, 81, 106), 
          (125, 185, 153), 
          (221, 86, 56), 
          (183, 150, 44), 
          (10, 48, 92), 
          (135, 35, 47), 
          (197, 128, 159), 
          (208, 215, 11), 
          (72, 45, 32), 
          (36, 62, 42), 
          (25, 60, 123), 
          (122, 41, 34),
          (25, 169, 141), 
          (19, 91, 49), 
          (152, 206, 213), 
          (31, 176, 185), 
          (155, 207, 191), 
          (83, 77, 36), 
          (221, 174, 186)]

