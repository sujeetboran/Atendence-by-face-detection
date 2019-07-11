from mtcnn.mtcnn import mtcnn
import os
import glob
import cv2

detector=MTCNN()
#give the path of a group photo
path="group/image"
image=cv2.imread(path,0)
detect_faces=detector.detect_faces(image)
i=0
for faces in detect_faces:
  i=i+1
  x1, y1, width, height = detect_faces[0]['box']
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	face = pixels[y1:y2, x1:x2]
  path_of_face=path+str(i)
  cv2.imwright(path_of_face,face)