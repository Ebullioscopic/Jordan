# # program to capture single image from webcam in python 

# # importing OpenCV library 
# from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow

# # initialize the camera 
# # If you have multiple camera connected with 
# # current device, assign a value in cam_port 
# # variable according to that 
# cam_port = 0
# cam = VideoCapture(cam_port) 

# # reading the input using the camera 
# result, image = cam.read() 

# # If image will detected without any error, 
# # show result 
# if result: 

# 	# showing result, it take frame name and image 
# 	# output 
# 	imshow("GeeksForGeeks", image) 

# 	# saving image in local storage 
# 	imwrite("GeeksForGeeks.png", image) 

# 	# If keyboard interrupt occurs, destroy image 
# 	# window 
# 	waitKey(0) 
# 	destroyWindow("GeeksForGeeks") 

# # If captured image is corrupted, moving to else part 
# else: 
# 	print("No image detected. Please! try again") 
'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from cv2 import imread
from deepface import DeepFace
import numpy
from PIL import Image
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (1080, 720)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
        #on_release: root.recognize()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG.png")
        #textu = camera.texture
        print("Captured")
        img = imread("IMG.png")
        result = DeepFace.analyze(img, 
						actions = ['emotion'], enforce_detection=False) 
        print(result[0]["dominant_emotion"])
# print result 
        print(result)


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()