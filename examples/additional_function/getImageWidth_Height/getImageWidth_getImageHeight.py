# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# get width image (pixels)
width = moildev.getImageWidth()

# print value
print("width = ", width)

# get Height image (pixels)
height = moildev.getImageHeight()

# print value
print("height = ", height)
