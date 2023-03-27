import cv2
from copy import deepcopy
import numpy as np


class Contour:
    def __init__(self, image=None):
        self.__image = image
        self.__contours = None
        self.__hierarchy = None
        self.__img = None
        self.__algorithm = []

    def set(self, image):
        self.__image = image
        return self

    def get(self):
        return self.__image

    # to edge detection
    def to_canny(self, thr=[50, 150], a_size=3):
        self.__algorithm.append('to_canny')
        self.__image = cv2.Canny(self.__image, thr[0], thr[1], apertureSize=a_size)
        return self

    # to increase ones
    def to_dilate(self, kernel=(5, 5), iterations=3):
        self.__algorithm.append('to_dilate')
        dilate_kernel = np.ones(kernel)
        self.__image = cv2.dilate(self.__image, dilate_kernel, iterations)
        return self

    # increase zeros
    def to_erode(self, kernel=(5, 5), iterations=3):
        self.__algorithm.append('to_erode')
        erode_kernel = np.ones(kernel)
        self.__image = cv2.erode(self.__image, erode_kernel, iterations)
        return self

    def to_morphopen(self, kernel=(5, 5)):
        self.__algorithm.append('to_morphopen')
        self.__image = cv2.morphologyEx(self.__image, cv2.MORPH_OPEN, kernel)
        return self

    def to_morphclose(self, kernel=(5, 5)):
        self.__algorithm.append('to_morphclose')
        self.__image = cv2.morphologyEx(self.__image, cv2.MORPH_CLOSE, kernel)
        return self

    def to_morphgradient(self, kernel=(5, 5)):
        self.__algorithm.append('to_morphgradient')
        self.__image = cv2.morphologyEx(self.__image, cv2.MORPH_GRADIENT, kernel)
        return self

    def to_morphtophat(self, rect_kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))):
        self.__algorithm.append('to_morphtophat')
        self.__image = cv2.morphologyEx(self.__image, cv2.MORPH_TOPHAT, rect_kernel)
        return self

    def to_threshold(self, thr=[150, 255]):
        self.__algorithm.append('to_threshold')
        ret, self.__image = cv2.threshold(self.__image, thr[0], thr[1], cv2.THRESH_BINARY)
        return self

    def to_adaptive_threshold(self, block_size=21, c=7):
        self.__algorithm.append('to_adaptive_threshold')
        self.__image = cv2.adaptiveThreshold(self.__image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                             block_size, c)
        return self

    def find(self):
        self.__contours, self.__hierarchy = cv2.findContours(self.__image.get(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return self

    def contours(self):
        return self.__contours

    def hierarchy(self):
        return self.__hierarchy

    def draw(self, color=(0, 255, 0), thickness=2):
        cv2.drawContours(self.__image.original(), self.__contours, -1, color, thickness)
        self.__image.set(self.__image.original())
        return self

    def return_image(self):
        from src.image import Image
        if self.__img is None:
            self.__img = Image()
        self.__img.set(self.__image)
        return self.__img