import numpy as np
import cv2
from src.image import Image
from src.video import Video


vid = Video()
vid.path('assets/videos/test2103-0.avi')
while True:
    vid.read().image().\
        convert().\
        to_gray().\
        return_image().\
        show(name = "Gray").\
        contour().to_canny().\
        return_image().\
        show()

    cv2.imshow('vid',vid.get())
    if cv2.waitKey(20) == ord('q'):
        break

cv2.destroyAllWindows()