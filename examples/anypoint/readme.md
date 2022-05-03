## Anypoint image example code
> In order to run this example, please understand how to [create object](../Create_object) of moildev and need installation of [opencv library](https://pypi.org/project/opencv-python/)
## overview
This example demonstrated how to generate **undistotion image** or **anypoint view image** using **getAnypointMaps()** and **anypoint()** function. For mode 1, the result rotation is betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). for mode 2, The result rotation is theta_Y degree rotation around the Y-axis(yaw) after theta_X degree rotation around the X-axis(pitch).

Moildev provide **two option** to create anypoint image, you only need to **choose one**:
1. getAnypointMaps()
> This function will create give you return maps x and maps y for specified zenital and azimutal angel. return of X-Y Maps can be use later to remap the original image to undistortion image. by default this function will give you anypoint mode-1. You can use *opencv remap* to create anypoint image.
2. anypoint()
> This function will give you undistortion image or anypoint image directly without using remap function anymore.
### variable
> - image: source image
> - alpha: the value of alpha
> - beta: the value of beta
> - zoom: decimal zoom factor, normally 1 to 12
> - mode: mode anypoint view (by default it will be mode 1)

### Python function
getAnypointMaps function
> map_x, map_y = moildev.getAnypointMaps(alpha, beta, zoom, mode=1)

output 
> maps_x, maps_y

anypoint function
>anypoint_image = moildev.anypoint(image, alpha, beta, zoom, mode=1)

output
>anypoint image

## Code Overview
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
# create specified variable value of alpha beta zoom and mode
alpha = 30
beta = 30
zoom = 4
mode = 2
```
Read image from directory
```python
# read image from directory using opencv
image = cv2.imread("../image.jpg")
```
### You only need choose one between this two function
1. create anypoint image using getAnypointMaps and remap function

After get maps x and maps y, next add function [cv2.remap](https://docs.opencv.org/3.4/d1/da0/tutorial_remap.html) from opencv

```python
# create maps_x and map_y image
map_x, map_y = moildev.getAnypointMaps(alpha, beta, zoom, mode)
# create anypoint image using remap function from map x and map y
anypoint_image_1 = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
```
2. Create anypoint using anypoint function image

Directly create anypoint image in one line code
```python
# create anypoint image
anypoint_image = moildev.anypoint(image, alpha, beta, zoom, mode)
```
Save image using opencv cv2.imwrite
```python
# save anypoint image
cv2.imwrite("anypoint_image_1.jpg", anypoint_image_1)
cv2.imwrite("anypoint_image_2.jpg", anypoint_image_2)
```

Result:

Image Anypoint result will be the same between getAnypointMaps() and anypoint()

| input image       | Output image
|-------------------| --- 
| ![](../image.jpg) | ![](img/result.jpg)