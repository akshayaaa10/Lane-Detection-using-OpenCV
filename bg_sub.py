import cv2
import numpy as np

cap =cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
while True:
    ret, frame = cap.read()
    if frame is None :
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()