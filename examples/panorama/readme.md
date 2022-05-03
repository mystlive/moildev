## Panorama image example code
> In order to run this example, please understand how to [create object](../Create_object) of moildev and need installation of [opencv library](https://pypi.org/project/opencv-python/)
## overview
This example demonstrated how to generate panorama image centered at the 3D direction with alpha = iC_alpha_degree and beta = iC_beta_degree.
 
Moildev provide two option to create panorama image. you only need to choose one:
1. getPanoramaMaps()
> This function will give you return maps x and maps y for panorama image. after get maps x and maps y we can create panorama image using remap function from opencv.
2. panorama()
> This function will give return a panorama image directly.

## variable
> - image = the original image
> - alpha_min = the minimum alpha
> - alpha_max : max of alpha. The recommended value is half of camera FOV.

#### Python function
Remember to choose only one:

1. getPanoramaMaps() function
> map_x, map_y = moildev.getPanoramaMaps(alpha_min, alpha_max)

output:
> maps-x and maps-y
2. panorama() function
> panorama_image = moildev.panorama(image, alpha_min, alpha_max)

output:
> panorama image

These two function was working in the same output image panorama.
## code Overview
first, import and create object of moildev library
```python
# import library
import cv2
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)
``````
Create specified variable value of alpha, beta, zoom and mode
```python
# create specified variable value of alpha min dan alpha max
alpha_min = 10
alpha_max = 110
```
Read image from directory
```python
# read image from directory using opencv
image = cv2.imread("../image_2.png")
```
1. Create maps and panorama image using remap function

After get maps x and maps y, next add function [cv2.remap](https://docs.opencv.org/3.4/d1/da0/tutorial_remap.html) from opencv
```python
# create maps_x and map_y image
map_x, map_y = moildev.getPanoramaMaps(alpha_min, alpha_max)
panorama_image_1 = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
```
2. Create panorama image directly image
```python
# create panorama image
panorama_image = moildev.panorama(image, alpha_min, alpha_max)
```
Save image using opencv imwrite
```python 
# save panorama image
cv2.imwrite("panorama_image_1.jpg", panorama_image_1)
cv2.imwrite("panorama_image_2.jpg", panorama_image_2)
```

Result:

Image result of Panorama will be same between getPanoramaMaps() and panorama()

| input image         | Output image
|---------------------| --- 
| ![](../image_2.png) | ![](img/result.jpg)

