
import cv2
import os
import numpy as np
import time

def colorDetection(image, i):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    '''yellow'''
    # Range for upper range
    yellow_lower = np.array([20, 90, 100])
    yellow_upper = np.array([100, 255, 255])
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    yellow_output = cv2.bitwise_and(image, image, mask=mask_yellow)
    # Drawing
    lineThickness = 8
    yellow_output = cv2.line(yellow_output, (100, 100), (20000, 20000), (0,0,255), lineThickness)
    cv2.imwrite(f"yellow{i}.png", yellow_output)
    yellow_ratio =(cv2.countNonZero(mask_yellow))/(image.size/3)

    print("Yellow in image", np.round(yellow_ratio*100, 2))


#frame = cv2.imread("/users/stephen/Documents/Github/Vision-Python/test.jpeg")

"""for i, image in enumerate(os.listdir("images")):
    if (image.endswith(".jpeg")):
        img = cv2.imread('/users/stephen/Documents/Github/Vision-Python/images/' + image)
        colorDetection(img, i)"""

img = cv2.imread("images/image4.jpeg")
print(img.shape)
#print(f"Height: {y}, Width: {x}")
t1 = time.time()
colorDetection(img, 4)
print(f"Took: {time.time()-t1} seconds")