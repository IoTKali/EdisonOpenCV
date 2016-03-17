import cv2.cv as cv  
capture = cv.CaptureFromCAM(0)  
img = cv.QueryFrame(capture)  
cv.SaveImage("aa1.jpg", img)  



 


























