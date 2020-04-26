import cv2
import os

f= open("shape.txt","w+")

directory = r'C:\Users\I341820\OneDrive - SAP SE\Desktop\Assignment-13\yolo\YoloV3\data\customdata\images'
for filename in os.listdir(directory):
		
	# read image
	direc=directory+'\\'+filename
	img = cv2.imread(direc)
	print(img)
	# get dimensions of image
	dimensions = img.shape
	# height, width, number of channels in image
	height = img.shape[0]
	width = img.shape[1]
	channels = img.shape[2]
	stri=str(width)+" "+str(height)+'\n'
	f.write(stri)

f.close()
