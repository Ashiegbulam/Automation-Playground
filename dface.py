"""AI for detecting faces in pictures and real time"""
import cv2
from random import randrange as rr

# loads pre-trained data(.xml) to classifier which in turn detects front faces
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# """working on images"""
# work = ['Media/obama.jpg', 'Media/Elon.jpg']
# img = cv2.imread(work[0]) # reads image from list

# # converts img specimen to grayscale (required to help the algorithm perform better by dealing with b&w only)
# grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # in opencv its the inverse of rgb

# detects faces in img specimen by returning its coordinates (detectMultiScale = detect any size of face)
# face_coordinates = trained_face_data.detectMultiScale(grayscale_img)
# # print(face_coordinates)

# # draw rectangles around faces in the coloured(normal) image 
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (rr(256), rr(256), rr(256)), 3)

# cv2.imshow('Face Detector Program', img) # display image
# cv2.waitKey() # program waits until a key is pressed before it closes else it closes in split seconds


"""On webcam/video"""
webcam = cv2.VideoCapture(0) #to capture videeo from camera (pass video path to read specific video)

# iterate over frames to implement detection throughout video
while True:
    successful_frame_read, frame = webcam.read() # read current frame
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
    face_coordinates = trained_face_data.detectMultiScale(grayscale_frame) # detects faces in img specimen by returning its coordinates
    
    # draw rectangles around faces in the coloured(normal) frame
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (rr(256), rr(256), rr(256)), 3)
    
    cv2.imshow('OG', frame) 
    key = cv2.waitKey(1) #waits infinetly for a key to be pressed to move to anther frame. Passing (1) makes it wait 1 millisecond instead

    # stop if S key is pressed
    if key==83 or key==115: # digits are gotten from corresponding ascii character codes
        break

webcam.release() # to release the videocapture object