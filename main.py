import numpy as np
import cv2
from src.image import Image
from src.video import Video

# img = Image()

# img.show().wait()

# img.path('assets/image/main.png').\
#     convert().to_gray().return_image().\
#     contour().to_canny().return_image().\
#     show().wait()


vid = Video()
vid.path('assets/videos/test1_1602.avi')
while True:
    vid.read().image().\
        convert().\
        to_gray().\
        return_image().\
        contour().to_canny().\
        return_image().\
        show()

    cv2.imshow('a',vid.get())
    if cv2.waitKey(1) > 0 :
        break

cv2.destroyAllWindows()