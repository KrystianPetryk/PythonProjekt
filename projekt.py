import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from PIL import Image
import math

import imgproc

points=[]
img=cv2.imread("foto.jpg")
img_cpy=img.copy()
# Zmiana skali wyświetlania w resize_factor jeśli rozmiar zbyt duży lub za mały
h,w = img.shape[:2]
#zwiększanie wartości powoduje zmniejszenie wyswietlanego obrazu
resize_factor=math.sqrt(1)
h = int(h / resize_factor)
w = int(w / resize_factor)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', (w,h))

cv2.imshow("image", img_cpy)

def add_point(event, x, y, flags, param):
    if event== cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img_cpy, (x, y), 3, [0,0,225], -1)

        if len(points) == 4:
            height = 640
            width=480
            ref_points= [(0,0), (width-1, 0), (width-1, height-1), (0, height-1)]
            params=imgproc.find_transformation(points, ref_points )
            rectified_img = imgproc.correct_perspective(img, params, width, height)
            cv2.imshow("rectified image", rectified_img)
            cv2.imwrite("correct.jpg", rectified_img)


cv2.setMouseCallback("image", add_point)

while True:
    cv2.imshow("image", img_cpy)
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
