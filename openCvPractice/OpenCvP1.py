import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')   #this command used to clear the terminal
#img=cv2.imread(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\PYTHON\openCvPractice\watch.jpg",cv2.IMREAD_GRAYSCALE)

##loading images##
#cv2.imshow("image",img)
#cv2.waitKey (0)
#cv2.destroyAllWindows()

##loading images and drawing a line,drawing a rectangle,filling a rectangle,drawing a circle,filling a rectangle ##
#cv2.line(img,(15,15),(150,150),(0,0,0),5)     #the first brackets is for the starting point,the second for the ending point,third for the color ,the last one for the thichkness
#cv2.rectangle(img,(14,30),(200,370),(255,255,255),3)  #the first bracekts tells us the left most corner ,the second one tells us the bottomost right corner,third one for color,the last one for thickness.Here the brackets for color follows BGR.
#cv2.circle(img,(90,78),66,(255,255,255),0)  #the first bracets tells us about the centre of the circle,the second one about the radius of the circle,the third one about the thicknes and if u put a negative no.into it it will fill the whole with the given colo as input.
#to make our own requiremental polygon
#pts=np.array([[20,40],[34,89],[45,67]],np.int32)   #here we take a an array points to make a polygon 
#cv2.polylines(img,[pts],True,(255,255,255),0)     #here the points are given in the form of an array and true is givewn to wether to join all the points and false is given to not join the last line and the next brackets are for colo=r,the last one is for thickness.

#writing text on a image
#font=cv2.FONT_HERSHEY_COMPLEX    #here we give the type of font we want.
#cv2.putText(img,'OpenCv Tuts!',(0,45),font,1,(255,255,255),2,cv2.LINE_AA)    #here we give the title name,the position,the,font,the spacing,the color,the thickness.

#cv2.imshow("image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


##loading image and ploting them##
#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([50,100],[40,50],"c",linewidth=5)
#plt.show()

##capturing video##

#face=cv2.VideoCapture(0)
#fourrc=cv2.VideoWriter(*'XVID')
##out=cv2.VideoWriter('output.avi',fourrc)
##out.set(cv2.CAP_PROP_FRAME_WIDTH,320)
##out.set(cv2.CAP_PROP_FRAME_HEIGHT,180)
##out.set(cv2.CAP_PROP_FPS,25)

#while True:
#    ret, frame=face.read()
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    cv2.imshow('frame',frame)
#    cv2.imshow('gray',gray)
#    out.write(frame)
#    if cv2.waitKey(1) & 0xFF==ord('q'):
#        break
#face.release()
#out.release()
#cv2.destroyAllWindows()



##to chnage the color of the at a particular point or a particular space##

#img[50,50]=[255,255,255]                #this is convert the point color intop different one. 
#img[130:180,120:180]=[255,255,255]      #this is yo convert the given space into given color.
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



##taking a particular space from a image and copyiong and pasting it into the given other space

#watch_face=img[100:150,150:200]     #here we should make sure that the given space is equal to the space provided to copy that image. 
#img[0:50,0:50]=watch_face
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


##adding two images into one.##

#img1=cv2.imread(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\PYTHON\openCvPractice\ss1.png")
#img2=cv2.imread(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\PYTHON\openCvPractice\plogo.png")
#add=cv2.add(img1,img2)    #this fucntion is two add two images.
#weighted=cv2.addWeighted(img1,0.8,img2,0.3,0)   #the first value tells us about the percentage of the image to be loaded and similarly the second one.
###from here on the code is made to add two images if they arent in same size also and change their pixels also....
#rows,cols,channels=img2.shape
#roi=img1[0:rows,0:cols]
#img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)   #this line of code converts it into grayscale.
#ret,mask=cv2.threshold(img2gray,200,190,cv2.THRESH_BINARY_INV)    #this line of code is to convert the pixel into different one if it exceeds the firwst value and second value is the pixel value assignied to it.
#mask_inv=cv2.bitwise_not(mask)
#img_2=cv2.bitwise_and(img2,img2,mask=mask)
#img_1=cv2.bitwise_and(roi,roi,mask=mask_inv)
#dst=cv2.add(img_1,img_2)
#img1[0:rows,0:cols]=dst
#cv2.imshow("res",img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


##THRESHOLDING##
#img1=cv2.imread(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\PYTHON\openCvPractice\lowlightpic.png")
#retval,threshold=cv2.threshold(img1,12,255,cv2.THRESH_BINARY)
#grayscale=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#retval,graythresh=cv2.threshold(img1,12,255,cv2.THRESH_BINARY)
#gaus=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#retval2,ostu=cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imshow("original",img1)
#cv2.imshow("threshold",threshold)
#cv2.imshow("graythresh",graythresh)
#cv2.imshow("ostu",ostu)
#cv2.imshow("gaus",gaus)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



##color filtering##
cap=cv2.VideoCapture(0)

#while True:
#    _,frame=cap.read()
#    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#    lower_red=np.array([150,150,50])
#    upper_red=np.array([180,255,150])
#    mask=cv2.inRange(hsv,lower_red,upper_red)
#    res=cv2.bitwise_and(frame,frame,mask=mask)
#    kernel=np.ones((15,15),np.float32)/255    ###these two lines are smoothening .....
#    smoothed=cv2.filter2D(res,-1,kernel)
#    cv2.imshow("frame",frame)
#    cv2.imshow("mask",mask)
#    cv2.imshow("res",res)
#    k=cv2.waitKey(5) & 0xFF
#    if k==27:
#        break
#cv2.destroyAllWindows()
#cap.release()


##edge detection##
while True:
    _,frame=cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    cv2.imshow('original',frame)
    cv2.imshow('lpalacian',laplacian)
    k=cv2.waitKey(5) and 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()