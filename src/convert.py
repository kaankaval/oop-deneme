import cv2
from image import image

class Convert:
    def __init__(self,i=None):
        self.__image = i
        self.__converted = None
        self.__algorithm = []

    # set image array
    def set(self, image_set):
        self.__algorithm.append('set')
        self.__image = image_set
        return self

    # get image array
    def get(self):
        self.__algorithm.append('get')
        return self.__converted

    # ----------------------------------ColorSpaces-------------------------------#

    # convert to gray
    def to_gray(self):
        self.__algorithm.append('to_gray')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
        return self

    # convert to HSV
    def to_hsv(self):
        self.__algorithm.append('to_hsv')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2HSV)
        return self

    # convert to HLS
    def to_hls(self):
        self.__algorithm.append('to_hls')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2HLS)
        return self

    # convert to lab
    def to_lab(self):
        self.__algorithm.append('to_lab')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2LAB)
        return self

    # convert to YCrCb
    def to_ycrcb(self):
        self.__algorithm.append('to_ycrcb')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2YCrCb)
        return self

    # convert to BGRA
    def to_bgra(self):
        self.__algorithm.append('to_bgra')
        self.__converted = cv2.cvtColor(self.__image, cv2.COLOR_BGR2BGRA)
        return self
    # ----------------------------------ColorSpacesEnd-------------------------------#
    # ----------------------------------ImageFunctions-------------------------------#
    # blur image
    def to_blur(self, kernel=(5, 5)):
        self.__algorithm.append('to_blur')
        self.__converted = cv2.blur(self.__image, kernel)
        return self

    def to_gaussian_blur(self, kernel=(5, 5), iterations=3):
        self.__algorithm.append('to_gaussian_blur')
        self.__converted = cv2.GaussianBlur(self.__image, kernel, iterations)
        return self

    def to_bilateral_blur(self, d=11, s_color=150, s_space=150):
        self.__algorithm.append('to_bilateral_blur')
        self.__converted = cv2.bilateralFilter(self.__image, d, s_color, s_space)
        return self

    def to_median_blur(self, k=9):
        self.__algorithm.append('to_median_blur')
        self.__converted = cv2.medianBlur(self.__image, k)
        return self