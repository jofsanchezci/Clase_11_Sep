from PIL import Image
import numpy as np
import random


# Create a 100x100 pixel image with a pure red color
width, height = 100, 100
R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)
print(R,G,B)


red_image = np.zeros((height, width, 3), dtype=np.uint8)
red_image[:] = [R, G, B]  # R = 255, G = 0, B = 0

# Convert the NumPy array to an image and save it
image = Image.fromarray(red_image)
image.save('red_image.png')