import cv2
import numpy as np


class Video:
    def __init__(self,path):
        self.__path = path
        self.__video = cv2.VideoCapture(path)
        self.__frame = None
        self.__algorithm = []

    #set video capture
    def set(self,video_set):
        self.__algorithm.append('set')
        self.__video = video_set
        return self

    # set video capture
    def frame_set(self, frameset):
        self.__algorithm.append('frameset')
        self.__frame = frameset
        return self

    #get video capture
    def get(self):
        self.__algorithm.append('get')
        return self.__video

    def width(self):
        self.__algorithm.append('width')
        width = int(self.__video.get(3))
        return width

    def height(self):
        self.__algorithm.append('heigth')
        height = int(self.__video.get(4))
        return height

    #read video frame
    def from_read(self):
        self.__algorithm.append('read')
        ret, self.__frame = self.__video.read()
        return ret, self.__frame

    #release video capture
    def release(self):
        self.__algorithm.append('release')
        self.__video.release()
        return self