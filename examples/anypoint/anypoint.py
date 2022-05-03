# import library
import cv2
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../data/Raspi_Cam.json")  # select parameter file (.json)

# create specified variable value of alpha beta zoom and mode
alpha = 45
beta = 0
zoom = 4
mode = 2

# read image from directory using opencv
image = cv2.imread("../data/image.jpg")

# create maps_x and map_y image
map_x, map_y = moildev.getAnypointMaps(alpha, beta, zoom, mode)

# create anypoint image using remap function from map x and map y
anypoint_image_1 = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)

# create anypoint image
anypoint_image_2 = moildev.anypoint(image, alpha, beta, zoom, mode)  # fill the variable

# save anypoint image
cv2.imwrite("reanypoint_image_1.jpg", anypoint_image_1)
cv2.imwrite("anypoint_image_2.jpg", anypoint_image_2)
