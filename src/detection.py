################################################################################
# Diagram localization
################################################################################

import numpy as np
import cv2 as cv


def get_diagram_position(color_image):
    assert isinstance(color_image, (np.ndarray, np.generic)), "color_image must be a numpy array"

    # preprocessing
    image = cv.cvtColor(color_image, cv.COLOR_BGR2GRAY)
    image = cv.adaptiveThreshold(image.astype(np.uint8),
                                 255,
                                 cv.ADAPTIVE_THRESH_MEAN_C,
                                 cv.THRESH_BINARY,
                                 11,
                                 3)
    image = 255 - image
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
    image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    
    #crop diagram
    contours, h = cv.findContours(image,
                                  cv.RETR_TREE,
                                  cv.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv.contourArea)
    x, y, w, h = cv.boundingRect(contour)
    return x, y, w, h
