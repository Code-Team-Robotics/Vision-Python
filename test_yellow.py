
import cv2
import os
import numpy as np
import time

def colorDetection(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    '''yellow'''
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    # Does an 'and' bitwise operation on the image so that the values get zeroed out...
    yellow_output = cv2.bitwise_and(image, image, mask=mask_yellow)
    # Drawing
    #qlineThickness = 8
    #yellow_output = cv2.line(yellow_output, (100, 100), (20000, 20000), (0,0,255), lineThickness)
    #cv2.imwrite(f"yellow{i}.png", yellow_output)
    #yellow_ratio =(cv2.countNonZero(mask_yellow))/(image.size/3)

    #print("Yellow in image", np.round(yellow_ratio*100, 2))
    return yellow_output

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

yellow_lower = np.array([30, 100, 110])
yellow_upper = np.array([101, 260, 260])
i = 0
time.sleep(3)
cap = cv2.VideoCapture(1)
while True:
    time.sleep(1)
    ret, frame = cap.read()
    frame = colorDetection(frame, yellow_lower-i, yellow_upper+i)
    cv2.imshow('Testing',frame)
    print(f"Lower: {yellow_lower-i}, Upper: {yellow_upper+i}")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1

cap.release()
cv2.destroyAllWindows()

