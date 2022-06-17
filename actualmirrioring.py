import cv2
face=cv2.VideoCapture(0)
while True:
    ret, frame=face.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
face.release()
cv2.destroyAllWindows()
