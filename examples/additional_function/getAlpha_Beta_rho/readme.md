## Get alpha beta example code
> In order to run this example, please understand how to [create object](../Create_object) of moildev and more information in [anypoint image](../anypoint)
## overview
This example demonstrated how to get alpha beta from delta_x and delta_y (position of pixel in image)

### variable
> - delta_x = pixel position of the image in x-axis
> - delta_y = pixel position of the image in y-axis 
> - alpha = for create anypoint image 
> - rho = degree 

### Python function
getAlphaBeta function
> alpha, beta = moildev.getAlphaBeta(delta_x, delta_y, mode=1)

anypoint function
>alpha = moildev.getAlphaFromRho(rho)

anypoint function
>rho = moildev.getRhoFromAlpha(alpha)

These two function was working in the same output. for create anypoint image we need to create maps first, after that we can use remap function to create anypoint image from fisheye images.
## Code Overview
first, import and create object of moildev library
```python
# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)
``````
Create specified variable value of alpha, beta, zoom and mode
```python
# create specified variable value
delta_x = 1652
delta_y = 592
mode = 1
rho_to_alpha = 520
alpha_to_rho = 40
```

1. Get alpha beta from input delta_x and delta_y
```python
# get alpha beta from input delta_x and delta_y
alpha, beta = moildev.getAlphaBeta(delta_x, delta_y, mode)  # fill the variable
# print alpha and beta
print(alpha, beta)
```
output :
> alpha =   38.2 ,beta =  43.42633594589745

2. Get alpha from rho
```python
# get alpha from rho
alpha_from_rho = moildev.getAlphaFromRho(rho_to_alpha)
# print alpha
print('alpha = ', alpha_from_rho)
```
output:
> alpha =  38.7

3. Get rho from alpha
```python
rho_from_alpha = moildev.getRhoFromAlpha(alpha_to_rho)
# print rho
print('rho = ', rho_from_alpha)
```
output:
> rho = 535.45255948587