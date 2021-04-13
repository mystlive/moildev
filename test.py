from Moildev import Moildev
import cv2

image = cv2.imread("image.jpg")
moildev = Moildev("Raspi_Cam.json")
alpha, beta = moildev.get_alpha_beta(900, 0, 1)
image = moildev.anypoint(image, alpha,beta,4, 1)

resized_image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
cv2.imshow("Result", resized_image)
cv2.waitKey()
