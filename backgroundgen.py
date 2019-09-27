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

shading = np.sin(np.arange(height) * 1/float(height) * np.pi + np.pi/2) * 55 + 200
array = np.transpose(np.array([shading, np.zeros(height), shading]))
print(array.shape)
print(img[:,x_pos].shape)

strip_width = 4
#strip = (np.zeros(height, strip_width, 3) + 1) * array
for x in range (x_pos - strip_width/2, x_pos+strip_width/2 + 1):
	img[:,x] = array


cv2.imshow('background', img)
while (1):
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break

	elif key & 0xFF == ord('s'): 
		name = img_name.split('/')[1].split('.')[0] + '_' +sys.argv[2]
		ext = img_name.split('.')[1]
		filename = '{}.{}'.format(name,ext)
		cv2.imwrite('{}/{}'.format(img_name.split('/')[0],filename), img)

cv2.destroyAllWindows()