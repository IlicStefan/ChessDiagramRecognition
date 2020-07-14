################################################################################
# Diagram localization
################################################################################

import numpy as np
import cv2 as cv


def get_diagram_position(image):
    assert isinstance(image, (np.ndarray, np.generic)), "image must be a numpy array"

    # get the minimum bounding box for the chip image
    image = image[10:-10, 10:-10]
    imgray = cv.cvtColor(image, cv.COLOR_BGR2LAB)[..., 0]
    ret, thresh = cv.threshold(imgray, 20, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    mask = 255 - thresh
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    max_area = 0
    best = None
    for contour in contours:
        area = cv.contourArea(contour)
        if area > max_area:
            max_area = area
            best = contour

    rect = cv.minAreaRect(best)
    box = cv.boxPoints(rect)
    box = np.int0(box)

    # crop image inside bounding box
    scale = 1  # cropping margin, 1 == no margin
    W = rect[1][0]
    H = rect[1][1]

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)

    angle = rect[2]
    rotated = False
    if angle < -45:
        angle += 90
        rotated = True

    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
    size = (int(scale * (x2 - x1)), int(scale * (y2 - y1)))

    M = cv.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1.0)

    cropped = cv.getRectSubPix(image, size, center)
    cropped = cv.warpAffine(cropped, M, size)

    croppedW = W if not rotated else H
    croppedH = H if not rotated else W

    image = cv.getRectSubPix(
        cropped, (int(croppedW * scale), int(croppedH * scale)), (size[0] / 2, size[1] / 2))

    return image
