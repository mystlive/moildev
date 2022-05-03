## Get image width and height example code
> in order to run this example, please understand how to [create object](../Create_object) of moildev first.
## overview
This example demonstrates how to get width and height of fisheye image from parameter

## code overview
### [getImageWidth() and getImageHeight()](getImageWidth_getImageHeight.py)
First, import moildev library and create object
```python
# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)
```
1. Get Width and print the value
```python
# get width image (pixels)
width = moildev.getImageWidth()

# print value
print("width = ", width)
```
output:
> width =  2592
2. Get Icy and print the value
```python
# get Height image (pixels)
height = moildev.getImageHeight()

# print value
print("height = ", height)
```
output:
> height =  1944

