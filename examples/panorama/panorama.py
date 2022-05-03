# import library
import cv2
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# create specified variable value of alpha min and alpha max
alpha_min = 10
alpha_max = 110

# read image from directory using opencv
image = cv2.imread("../image_2.png")

# create maps_x and map_y image
map_x, map_y = moildev.getPanoramaMaps(alpha_min, alpha_max)
panorama_image_1 = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)

# create panorama image
panorama_image_2 = moildev.panorama(image, alpha_min, alpha_max)

# save panorama image
cv2.imwrite("panorama_image_1.jpg", panorama_image_1)
cv2.imwrite("panorama_image_2.jpg", panorama_image_2)
