
import cv2
#import emoji
import os
import numpy as np
import time

from PIL import Image


def colorDetection(image, i=0):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    '''yellow'''
    # Range for upper range
    yellow_lower = np.array([20, 100, 110])
    yellow_upper = np.array([100, 255, 255])
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    # Does an 'and' bitwise operation on the image so that the values get zeroed out...
    yellow_output = cv2.bitwise_and(image, image, mask=mask_yellow)
    output = cv2.cvtColor(yellow_output, cv2.COLOR_BGR2GRAY)
    # Drawing
    #qlineThickness = 8
    #yellow_output = cv2.line(yellow_output, (100, 100), (20000, 20000), (0,0,255), 20)
    #cv2.imwrite(f"yellow{i}.png", yellow_output)
    #yellow_ratio =(cv2.countNonZero(mask_yellow))/(image.size/3)

    #print("Yellow in image", np.round(yellow_ratio*100, 2))
    circles = cv2.HoughCircles(yellow_output, cv2.HOUGH_GRADIENT, 1.3, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
    return output

#frame = cv2.imread("/users/stephen/Documents/Github/Vision-Python/test.jpeg")

"""for i, image in enumerate(os.listdir("images")):
    if (image.endswith(".jpeg")):
        img = cv2.imread('/users/stephen/Documents/Github/Vision-Python/images/' + image)
        colorDetection(img, i)"""

"""img = cv2.imread("images/image4.jpeg")
print(img.shape)
#print(f"Height: {y}, Width: {x}")
t1 = time.time()
colorDetection(img, 4)
print(f"Took: {time.time()-t1} seconds")"""




cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = colorDetection(frame)
    cv2.imshow(f'YeLlOw',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

