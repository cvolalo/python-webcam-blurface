# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def find_and_blur(bw, color, myfaces, x, y, w, h): 
    # detect al faces
    faces = cascade.detectMultiScale(bw, 1.1, 4)
    print(faces)
    if len(faces) == 0:
        faces = myfaces
        print('no faces detected')
    # get the locations of the faces
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        # select the areas where the face was found
        roi_color = color[y:y+h, x:x+w]
        # blur the colored image
        blur = cv2.GaussianBlur(roi_color, (101, 101), 0)
        # Insert ROI back into image
        color[y:y+h, x:x+w] = blur            
    
    # return the blurred image
    return color,faces, x, y, w, h

# turn camera on
video_capture = cv2.VideoCapture(0)
faces, x, y, w, h = [0,0,0,0,0]
while True:
    # get last recorded frame
    
    _, color = video_capture.read()
    # transform color -> grayscale
    bw = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    # detect the face and blur it
    blur, faces, x, y, w, h = find_and_blur(bw, color,faces, x, y, w, h)
    # display output
    cv2.imshow('Video', blur)
    # break if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# turn camera off        
video_capture.release()
# close camera  window
cv2.destroyAllWindows()