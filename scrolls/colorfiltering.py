
import numpy as np
from PIL import Image
import cv2

def edit(fname,up):
    image = cv2.imread(fname)
    #cv2.imshow('frame', image)


    # It converts the BGR color space of image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold in HSV space
    lower = np.array([0, 0, 200])
    upper = np.array([up, 255, 255])

    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower, upper)

    # The black region in the mask has the value of 0,

    result = cv2.bitwise_and(image, image, mask = mask)
    out='mask '+str(upper)
    #cv2.imshow('frame', image)
    cv2.imshow(out, mask)
    cv2.imwrite('out.tif', mask)
    #cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


if __name__=='__main__':
    #edit('for testing.tif')
    edit('scroll1.tif',215)

