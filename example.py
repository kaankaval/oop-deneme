import numpy as np
import cv2
from src.image import Image
from src.video import Video
# from src.contour import Contour


image = Image('assets/image/main.png')
video = Video('assets/videos/test2103-0.avi') # W = 1280 H = 720

frame_count = 0
yarn_count = 0
yarn_count_ort = 0
yarn_arr = []

upper_height = 280
lower_height = 290
spacing = lower_height - upper_height
yarn_control_count = 149

'''
test0.avi == 151 iplik (149)
test1.avi == 145 iplik
test2.avi == 148 iplik
test3.avi == 148 iplik
'''

while True:
    retval, frame = video.from_read()

    if retval:

        w = video.width()
        cropped_image = frame[upper_height:lower_height,0:w]
        line_image = np.zeros((spacing, w+6), dtype=np.uint8)

        image.set(cropped_image)\
        .to_gray()\
        .to_blur(kernel=(3,3))\
        .to_morphtophat()\
        .show()\
        .to_threshold(thr=[50,255])\
        .show()

        ###############################drawing lines with array operations####################################
        for column in range(w):
            image_column = image.get()[:,column]
            white_count = np.count_nonzero(image_column == 255)

            if white_count < spacing/5 :
                line_image[:,column+2] = np.full((spacing,),0,dtype=np.uint8)

            if white_count >= spacing/5 :
                line_image[:, column+2] = np.full((spacing,),255,dtype=np.uint8)
        ######################################################################################################
        ##########################drawing lines with HoughlinesP function#####################################
        # lines = cv2.HoughLinesP(image.get(),rho= 1,theta= np.pi,threshold= 0, minLineLength= 10,maxLineGap= 1)
        #
        # # yarn_count=0
        # if lines is not None:
        #     for line in lines:
        #         for x1, y1, x2, y2 in line:
        #             if abs(x1 - x2) < 1:
        #                 cv2.line(line_image, (x1+2, 0), (x2+2, 30), (255, 255, 255), 1)
        #                 # yarn_count += 1
        ######################################################################################################
        ##########################Finding lines with array operations#########################################
        image.set(line_image)
        yarn_count = 0
        v_line = []
        for column in range(w):
            image_column = image.get()[:,column]

            x = np.count_nonzero(image_column == 255)
            if x < spacing/2 :
                next_column = image.get()[:, column+1]
                # prev_column_2 = image.get()[:,column-2]

                white_count = np.count_nonzero(next_column == 255)
                # prev_x_2 = np.count_nonzero(prev_column_2 == 255)

                white_count_sum = white_count #+prev_x_2

                if white_count_sum > spacing/2 :
                    if column not in v_line:
                        v_line.append(column)
                        cv2.line(frame, (column, upper_height), (column, lower_height), (0, 0, 255), 2)
                        yarn_count += 1
        ######################################################################################################
        ######################################Visiualizing####################################################
        yarn_arr.append(yarn_count)
        frame_count += 1

        if frame_count == 4: #take avarage on every 4 frames
            count_result = np.bincount(yarn_arr).argmax()
            frame_count = 0

            print(str(count_result))
            if count_result != yarn_control_count:
                print("!error!")
                cv2.waitKey(0)

            yarn_arr.clear()

        image.show()
        cv2.imshow('frame',frame)

        if cv2.waitKey(20) == ord('q'):
            break
        ######################################################################################################

video.release()
cv2.destroyAllWindows()