
import numpy as np
from PIL import Image
import cv2
import imutils

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
    return mask

def edge(image):
    
    edgeMap = imutils.auto_canny(image)
    cv2.imshow("Original", image)
    cv2.imshow("Automatic Edge Map", edgeMap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edgeMap

if __name__=='__main__':
    #edit('for testing.tif')
    im = cv2.imread('for testing.tif')
    masked = edit('for testing.tif',180)
    edges = edge(masked)
    
    print(edges.dtype)
    #unique, counts = np.unique(edges, return_counts=True)
    #print(np.asarray((unique,counts)).T)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.imshow(contours )
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    print("Number of Contours found = " + str(len(contours)))
    fun=contours
    for c in fun:
        vert=len(c)
        print('Number of vertices = '+str(vert))
        
            
    
    
    
    img_contours = np.zeros(masked.shape)
    # draw the contours on the empty image
    cv2.drawContours(img_contours, contours, -1, (255,255,255), 1)
    cv2.imshow('contours',img_contours )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(len(contours))
 