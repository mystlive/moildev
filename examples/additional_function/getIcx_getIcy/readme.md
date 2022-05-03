## Get image center x and image center y example code
> in order to run this example, please understand how to [create object](../Create_object) of moildev first.
## overview
This example demonstrates how to get Icx and Icy of fisheye image from parameter
- Icx = Image center in X-axis
- Icy = Image center in Y-axis

## code overview
### [getIcx() and getIcy()](getIcx_getIcy.py)
First, import moildev library and create object
```python
# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)
```
1. Get Icx and print the value
```python
# get center image x-axis (getIcx)
icx = moildev.getIcx()

# print value
print("icx = ", icx)
```
output:
> icx = 1298
2. Get Icy and print the value
```python
# get center image y-axis (getIcy)
icy = moildev.getIcy()

# print value
print("icx = ", icy)
```
output:
> icy = 966

