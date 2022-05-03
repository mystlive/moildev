## Import and Create Object example
> In order to run this example please do the installation of Moildev library first and make sure you have the parameter of camera

## overview
This example demonstrates how to create object of moildev and how to import the camera parameter.

Moildev had three deference way to create object. We just need to choose one
1. Create object using **input keyword arguments**
2. Create object using **one parameter** with json file format extension
3. Create object using **multiple parameter** with json file format extension

list of camera parameters keyword used to create objects:

>- cameraName = the name of the camera used
>- cameraFov = camera field of view (FOV)
>- sensorWidth = size of sensor width
>- sensorHeight = size of sensor height
>- icx = center image in x-axis
>- icy = center image in y-axis
>- ratio = the value of the ratio image
>- imageWidth = the size of width image
>- imageHeight = the size of height image
>- calibrationRatio = the value of calibration ratio
>- parameter0 .. parameter5= intrinsic fisheye camera parameter get from calibration

### [Check version and Create object of Moildev](create_object.py)
First, import Moildev Library
```python
from Moildev import Moildev
```
#### Check version of moildev library
```python
Moildev.version()
```

Output:
> This function will give you information about moildev version, last update, author and other

```commandline
===========================================
Name: Moildev-SDK for Python3 
Version: 0.1.0 
Last Update: 01 march 2022
Author: Haryanto 
Author-Email: haryanto@o365.mcut.edu.tw
Under license: Moil-Lab
===========================================
```

#### Create object
1. using keyword arguments
```python
moildev_1 = Moildev(cameraName="Raspi", cameraFov=220, sensorWidth=1.4, sensorHeight=1.4, icx=1298, icy=966, ratio=1,
                    imageWidth=2592, imageHeight=1944, calibrationRatio=4.05, parameter0=0, parameter1=0, parameter2=0,
                    parameter3=0, parameter4=-47.96, parameter5=222.86)
```
2. using one parameter with json file format extension
```python
moildev_2 = Moildev("../Raspi_Cam.json")
```
3. using multiple parameter with json file format extension. fill the parameter and camera type
```python
# create object with multiple camera parameter
moildev_3 = Moildev("../camera_parameters.json", camera_type="Raspi")  # select parameter file (.json)
```