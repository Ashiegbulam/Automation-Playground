"""AI to detect cars and pedestrians"""
import cv2
from random import randrange as rr


video = cv2.VideoCapture('Media/TeslaTest.mp4')
classifier_file = ['cars.xml', 'haarcascade_fullbody.xml'] 

# iterate over frames to implement detection throughout video
while True:
    (successful_read, frame) = video.read() # read current frame
    if successful_read: #for safe coding in case of unsuccessful read e.g manually stopping the video
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
    else:
        break

    for cp in classifier_file:
        tracker = cv2.CascadeClassifier(cp) # creating car/pedestrian classifier from pre-trained .xml haarcascades
        coordinates = tracker.detectMultiScale(grayscale_frame) # detects and return coordinates of cars and pedestrians
        """for visualisation"""
        # draw rectangles around cars and pedestrians in the coloured(normal) frame
        for (x, y, w, h) in coordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (rr(256), rr(256), rr(256)), 2)
    
    cv2.imshow('OG', frame) 
    key = cv2.waitKey(1) #waits infinetly for a key to be pressed to move to anther frame. Passing (1) makes it wait 1 millisecond instead

    # stop if S key is pressed
    if key==83 or key==115: # digits are gotten from corresponding ascii character codes
        break

video.release() # to release the videocapture object


"""Using classifier on images"""
# work = ['Media/car.jpg', 'Media/car2.jpg']
# classifier_file = 'cars.xml'

# img = cv2.imread(work[1]) # reads image from list
# gray_cars = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts image to grayscale (necessary for haarcascades)

# # creating car classifier from pre-trained cars.xml haarcascades
# car_tracker = cv2.CascadeClassifier(classifier_file)

# # detects cars in img by returning its coordinates (detectMultiScale = detect any size of cars)
# car_coordinates = car_tracker.detectMultiScale(gray_cars)

# # draw rectangles around cars in the coloured(normal) image 
# for (x, y, w, h) in car_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (rr(256), rr(256), rr(256)), 3)

# cv2.imshow('Traffic', img) #display image
# cv2.waitKey() #keep displaying until a key is pressed

