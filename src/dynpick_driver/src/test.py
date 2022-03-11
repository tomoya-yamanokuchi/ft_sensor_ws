import cv2
from cv2 import dnn_superres

# Create an SR object - only function that differs from c++ code
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('src/dynpick_driver/src/Logo.jpg')

# Read the desired model
rate = 3
path = "src/dynpick_driver/src/EDSR_x{}.pb".format(rate)
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
model_name = "edsr"
sr.setModel(model_name, rate)

# Upscale the image
result = sr.upsample(image)

# Save the image
cv2.imwrite("src/dynpick_driver/src/upscaled_{}_x{}.png".format(model_name, rate), result)