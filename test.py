from Moildev import Moildev
import cv2

image = cv2.imread("image.jpg")
moildev = Moildev("Raspi_Cam.json")
image = moildev.anypoint(image, 0,45,4, 2)

resized_image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
cv2.imshow("Result", resized_image)
cv2.waitKey()
