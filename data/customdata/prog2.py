import cv2
import os

f= open("dir.txt","w+")

directory = r'C:\Users\I341820\OneDrive - SAP SE\Desktop\Assignment-13\yolo\YoloV3\data\customdata\images'
for filename in os.listdir(directory):
		
	# read image
	
	stri='./data/customdata/images/'+filename+'\n'
	f.write(stri)

f.close()
