# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# get center image x-axis (getIcx)
icx = moildev.getIcx()

# print value
print("icx = ", icx)

# get center image y-axis (getIcy)
icy = moildev.getIcy()

# print value
print("icx = ", icy)

