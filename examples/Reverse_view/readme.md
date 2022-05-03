## Recenter image example code
> In order to run this example, please understand how to [create object](../Create_object) of moildev and need installation of [opencv library](https://pypi.org/project/opencv-python/)
## overview
This example demonstrated how to generate image with new center optical point.
### variable
> - image = The original fisheye image
> - alpha_max = max of alpha. The recommended value is half of camera FOV.
> - alpha = the value of alpha
> - beta = the value of alpha

### Python function
> reverse_image = moildev.reverseImage(image, alpha_max, alpha, beta)

## Code Overview
first, import and create object of moildev library
```python
# import library
import cv2
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)
``````
Create specified variable
```python
# create specified variable value of alpha beta zoom and mode
alpha_max = 110
alpha = 30
beta = 30
```
Read image from directory
```python
# read image from directory using opencv
image = cv2.imread("../image.jpg")
```
Create reverse image
```python
# create reverse image
reverse_image = moildev.reverseImage(image, alpha_max, alpha, beta)  # fill the variable
```
Save image using opencv cv2.imwrite
```python
# save reverse image
cv2.imwrite("reverse_image.jpg", reverse_image)
```
Result:

| input image       | Output image
|-------------------| --- 
| ![](../image.jpg) | ![](img/reverse_image.jpg)

