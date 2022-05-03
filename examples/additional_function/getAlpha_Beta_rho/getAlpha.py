# import library
from Moildev import Moildev

# create object of Moildev
moildev = Moildev("../Raspi_Cam.json")  # select parameter file (.json)

# create specified variable value
delta_x = 1652
delta_y = 592
mode = 1
rho_to_alpha = 520
alpha_to_rho = 40

# get alpha beta from input delta_x and delta_y
alpha, beta = moildev.getAlphaBeta(delta_x, delta_y, mode)  # fill the variable
# print alpha and beta
print("alpha =  ", alpha, ",beta = ", beta)

# get alpha from rho
alpha_from_rho = moildev.getAlphaFromRho(rho_to_alpha)
# print alpha
print('alpha = ', alpha_from_rho)

# get rho from alpha
rho_from_alpha = moildev.getRhoFromAlpha(alpha_to_rho)
# print rho
print('rho = ', rho_from_alpha)
