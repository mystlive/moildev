# import library
import cv2
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# create specified variable value
alpha_max = 110
alpha = 30
beta = 30

# read image from directory using opencv
image = cv2.imread("../image.jpg")

# create reverse image
reverse_image = moildev.reverseImage(image, alpha_max, alpha, beta)  # fill the variable

# save reverse image
cv2.imwrite("reverse_image.jpg", reverse_image)
