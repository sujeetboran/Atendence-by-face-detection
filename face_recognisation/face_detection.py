from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import cv2
import os
import glob

#extraction of faces

def extract_face(filename, required_size=(160, 160)):
	pixels=cv2.imread(filename)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	x1, y1, width, height = results[0]['box']
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	face = pixels[y1:y2, x1:x2]
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
  #returning the extracted face matrix
	return face_array

# path of the image
# for loop use to vsit every folder in folder and going for there images
def loading_data(path):
  face,name=list(),list()
  #
  for path_of_image_folder in os.listdir(path):
    path_of_image=path+'/'+path_of_image_folder
    for images in glob.glob(os.path.join(path_of_image, '*.jpg')):
      extracted_face= extract_face(images)
      extracted_face=cv2.cvtColor(extracted_face,cv2.COLOR_BGR2RGB)
      cv2.imwright(images)
      face.append(extracted_face)
      name.append(path_of_image_folder)
    path_of_image=path

#reading data from computer
trainX, trainy = load_dataset('traning_set')
testX, testy = load_dataset('test_set')

