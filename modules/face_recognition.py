#import the required modules 
import cv2 
from cv2 import VideoCapture
import matplotlib.pyplot as plt 
from deepface import DeepFace
# read image 
cam = VideoCapture(0)
#img = cv2.imread('C:\Job-Security\profile_big.jpg') 
res, img = cam.read()
# call imshow() using plt object 
#plt.imshow(img[:, :, : : -1]) 

# display that image 
#plt.show() 
# storing the result 
result = DeepFace.analyze(img, 
						actions = ['emotion']) 
print(result[0]["dominant_emotion"])
# print result 
print(result)