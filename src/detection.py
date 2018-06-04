################################################################################
# Diagram localization
################################################################################

import numpy as np
import cv2 as cv

def getDiagramPosition(color_img):
    #preprocessing
    img = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)
    img = cv.adaptiveThreshold(img.astype(np.uint8),
                               255,
                               cv.ADAPTIVE_THRESH_MEAN_C,
                               cv.THRESH_BINARY,
                               11,
                               3)
    img = 255 - img
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    
    #crop diagram
    _, contours, h = cv.findContours(img,
                                     cv.RETR_TREE,
                                     cv.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv.contourArea)
    x, y, w, h = cv.boundingRect(contour)
    return x, y, w, h
