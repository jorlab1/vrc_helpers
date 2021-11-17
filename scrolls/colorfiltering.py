
import numpy as np
from PIL import Image
import cv2

image = cv2.imread('for testing.tif')
cv2.imshow('frame', image)


    # It converts the BGR color space of image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
     
    # Threshold in HSV space
lower = np.array([0, 0, 200])
upper = np.array([180, 255, 255])
 
    # preparing the mask to overlay
mask = cv2.inRange(hsv, lower, upper)
     
    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes all non-blue regions
result = cv2.bitwise_and(image, image, mask = mask)
 
#cv2.imshow('frame', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
