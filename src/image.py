import cv2
from copy import deepcopy
import numpy as np
from src.convert import Convert
from src.contour import Contour


class Image:
    def __init__(self):
        self.__path = None
        self.__image = None,
        self.__original = None
        self.__algorithm = []
        self.__algorithm.append('init')

        self.__convert = None
        self.__contour = None
        self.__video = None

    # set image array
    def set(self, image_set):
        self.__algorithm.append('set')
        self.__image = image_set
        return self

    # get image array
    def get(self):
        self.__algorithm.append('get')
        return self.__image

    #get image path
    def path(self,path):
        self.__path = path
        self.__image = cv2.imread(self.__path)
        self.__original = deepcopy(self.__image)
        return self

    def convert(self):
        if self.__convert is None:
            self.__convert = Convert()
        self.__convert.set(self.__image)
        return self.__convert

    def contour(self):
        if self.__contour is None:
            self.__contour = Contour(self.__image)
        self.__contour.set(self.__image)
        return self.__contour

    def return_video(self):
        from src.video import Video
        if self.__video is None:
            self.__video = Video()
        self.__video.set(self.__image)
        return self.__video


    # ----------------------------------ImageOperations-------------------------------#
    # get image original array
    def original(self):
        self.__algorithm.append('original')
        return self.__original

    # show image
    def show(self,name=None):
        if name is None:
            name = self.__algorithm[-1]
        cv2.imshow(name, self.__image)
        self.__algorithm.append('show')
        return self

    # wait for key
    def wait(self,milisecond=0,key = ord('q')):
        self.__algorithm.append('wait')
        cv2.waitKey(milisecond)
        return self

    # get image weight
    def weight(self):
        self.__algorithm.append('weight')
        return self.__image.shape[0]

    # get image height
    def height(self):
        self.__algorithm.append('height')
        return self.__image.shape[1]

    # get image channel
    def channel(self):
        self.__algorithm.append('channel')
        return self.__image.shape[2]

    # show algorithm
    def algorithm(self):
        return self.__algorithm


if __name__ == '__main__':
    image = Image('../assets/image/ornek.png')
    image.show().wait()
    print(image.algorithm())