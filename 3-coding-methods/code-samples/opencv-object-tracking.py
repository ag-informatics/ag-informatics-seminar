## Code Source: https://machinelearningknowledge.ai/learn-object-tracking-in-opencv-python-with-code-examples/
## Class Contributor: Cheyenne

import cv2
import numpy as np


## KCF Object Tracking in OpenCV Python

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture('video.mp4')
ok,frame=video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame,bbox)

while True:
   ok,frame=video.read()
   if not ok:
        break
   ok,bbox=tracker.update(frame)
   if ok:
        (x,y,w,h)=[int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
   else:
        cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   cv2.imshow('Tracking',frame)
   if cv2.waitKey(1) & 0XFF==27:
        break
cv2.destroyAllWindows()


## CSRT Object Tracking in OpenCV Python

tracker = cv2.TrackerCSRT_create()
video = cv2.VideoCapture('video.mp4')
ok,frame=video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame,bbox)

while True:
    ok,frame=video.read()
    if not ok:
        break
    ok,bbox=tracker.update(frame)
    if ok:
        (x,y,w,h)=[int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
    else:
        cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow('Tracking',frame)
    if cv2.waitKey(1) & 0XFF==27:
        break
cv2.destroyAllWindows()


### Mean Shift Object Tracker Implementation in OpenCV Python

cap = cv2.VideoCapture('video.mp4')
ret,frame=cap.read()
x,y,w,h = cv2.selectROI(frame)
track_window = (x, y, w, h)
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
   ret, frame = cap.read()
   if ret == True:
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
       ret, track_window = cv2.meanShift(dst, track_window, term_crit)
       x,y,w,h = track_window
       img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
       cv2.imshow('img2',img2)
       k = cv2.waitKey(30) & 0xff
       if k == 27:
           break
   else:
       break
cv2.destroyAllWindows()


### Cam Shift Object Tracker Implementation in OpenCV Python

cap = cv2.VideoCapture('video.mp4')
ret,frame=cap.read()
x,y,w,h = cv2.selectROI(frame)
track_window = (x, y, w, h)
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
   ret, frame = cap.read()
   if ret == True:
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
       ret, track_window = cv2.CamShift(dst, track_window, term_crit)
       pts = cv2.boxPoints(ret)
       pts=np.int0(pts)
       img2 = cv2.polylines(frame, [pts], True, 255,2)
       cv2.imshow('img2',img2)
       k = cv2.waitKey(30) & 0xff
       if k == 27:
           break
   else:
       break
cv2.destroyAllWindows()