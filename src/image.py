import cv2
from copy import deepcopy
import numpy as np

from convert import Convert
from contour import Contour


class Image:
    def __init__(self, path):
        self.__path = path
        self.__image = cv2.imread(path)
        self.__original = deepcopy(self.__image)
        self.__algorithm = []

        self.__convert = Convert(self.__image)
        self.__contour = Contour(self.__image)


    # set image array
    def set(self, image_set):
        self.__algorithm.append('set')
        self.__image = image_set
        return self

    # get image array
    def get(self):
        self.__algorithm.append('get')
        return self.__image

    def set_convert(self):
        return self.__convert

    # def get_convert(self):
    #     self.__image = self.__convert.get()
    #     return self.__image

    def set_contour(self):
        return self.__contour

    # def get_convert(self):
    #     return self.__contour.get()

    # ----------------------------------ImageOperations-------------------------------#
    # get image original array
    def original(self):
        self.__algorithm.append('original')
        return self.__original

    # show image
    def show(self):
        cv2.imshow(self.__algorithm[-1], self.__image)
        self.__algorithm.append('show')
        return self

    # wait for key
    def wait(self):
        self.__algorithm.append('wait')
        cv2.waitKey(0)
        cv2.destroyAllWindows()
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