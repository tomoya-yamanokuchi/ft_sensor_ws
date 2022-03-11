import cv2

# Read image
name  = "upscaled_edsr_x3"
image = cv2.imread('src/dynpick_driver/src/{}.png'.format(name))

# result = cv2.medianBlur(image, 7)
# result = cv2.bilateralFilter(image, 9,75,75)

result = cv2.fastNlMeansDenoisingColored(
    src                = image,
    dst                = None,
    h                  = 10,
    hColor             = 10,
    templateWindowSize = 5,
    searchWindowSize   = 21
)

# Save the image
cv2.imwrite("src/dynpick_driver/src/filtered_{}.png".format(name), result)