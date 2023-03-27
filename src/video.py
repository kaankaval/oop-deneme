import cv2
import numpy as np
from copy import deepcopy
from src.image import Image


class Video:
    def __init__(self):
        self.__path = None
        self.__vid = None
        self.__frame = None
        self.__original = None
        self.__image = Image()

    def path(self,video_path):
        self.__path = video_path
        self.__vid = cv2.VideoCapture(self.__path)
        return self

    def set(self,frame):
        self.__frame = deepcopy(frame)
        self.__original = deepcopy(frame)
        return self

    def get(self):
        return self.__frame

    def original(self):
        return self.__original

    def read(self):
        self.__frame = self.__vid.read()[1]
        self.__original = deepcopy(self.__frame)
        return self

    def image(self):
        self.__image.set(self.__frame)

        return self.__image

