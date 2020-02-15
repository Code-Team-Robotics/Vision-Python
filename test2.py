import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# Video source - can be camera index number given by 'ls /dev/video*
# or can be a video file, e.g. '~/Video.avi'
cap = cv2.VideoCapture(1)
#frame = cv2.imread("/users/stephen/Documents/Github/Vision-Python/test.jpeg")
#print(type(frame[0][0]))
#print(type(frame))
while True:
	ret, frame = cap.read()
	for i, row in enumerate(frame):
		for j, column in enumerate(row):
			#if (i % 2 == 0) or (j %2 == 0):
				#continue
			#if sum(frame[i][j]) <= 500:
			#print(f"The sum is {sum([frame[i][j][0], frame[i][j][1]])}")
			#print(f"the value is {frame[i][j]}")
			if (frame[i][j][0] > 150) and (frame[i][j][1] > 100) (frame[i][j][2] > 50):
				pass
				
			else:
				#frame[i][j] = np.zeros((1,3))
				frame[i][j] = np.array([0,0,0])
	    # Our operations on the frame come here
	    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    #print("Got here")
	    # Display the resulting frame
	cv2.imshow("Modified", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()


#plt.figure()
"""
f, axarr = plt.subplots(2,1) 
f.suptitle("Comparing Images")
axarr[0].imshow(frame)
axarr[1].imshow(Image.open("/users/stephen/Documents/Github/Vision-Python/test.jpeg"))
#plt.imshow(frame)
#plt.imshow(Image.open("/users/stephen/Documents/Github/Vision-Python/test.jpeg"))
plt.show()"""