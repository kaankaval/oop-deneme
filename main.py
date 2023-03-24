import numpy as np
import cv2
from src.image import Image

img = Image('assets/image/main.png')

img.set_convert().to_gray()
img.show().wait()

img.set_convert().to_gray().turn_back().set_contour().draw_contours().turn_back().show().wait()