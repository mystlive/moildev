# import library
from Moildev import Moildev

# check version and other information
Moildev.version()

# create object using keyword arguments
moildev_1 = Moildev(cameraName="Raspi", cameraFov=220, sensorWidth=1.4, sensorHeight=1.4, icx=1298, icy=966, ratio=1,
                    imageWidth=2592, imageHeight=1944, calibrationRatio=4.05, parameter0=0, parameter1=0, parameter2=0,
                    parameter3=0, parameter4=-47.96, parameter5=222.86)

# create object with single parameter
moildev_2 = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# create object with multiple camera parameter
moildev_3 = Moildev("../camera_parameters.json", camera_type="Raspi")  # select parameter file (.json)

