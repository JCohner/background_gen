import cv2
import numpy as np
import sys
import os

# height = 1080
# width = 1920

#img = np.zeros((height, width ,3)).astype('uint8')
img_name = sys.argv[1]
print(img_name)
img = cv2.imread(img_name)
shape = img.shape
width = shape[1]
height = shape[0]

x_pos = int(5 * width / 6.0)

cv2.line(img, (x_pos, 0), (x_pos, height), (255, 0 ,255), 4)

cv2.imshow('background', img)
while (1):
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break

	elif key & 0xFF == ord('s'): 
		name = img_name.split('/')[1].split('.')[0] + sys.argv[2]
		ext = img_name.split('.')[1]
		filename = '{}.{}'.format(name,ext)
		cv2.imwrite('backgrounds/{}'.format(filename), img)

cv2.destroyAllWindows()