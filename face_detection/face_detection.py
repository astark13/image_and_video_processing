import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,             # this "function" analyzes the image multiple times, each time decreasing its size with 5%                      
minNeighbors=5)     

for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)   # draws a rectangle based on the upper left corner (x,y)\
                                                         # lower right corner (x+w,y+h); the line color is green \
                                                         # (0,255,0) and the widht of the line is 3 pixels  

print(type(faces))  #class 'numpy.ndarray'
print(faces)        # output [[157  84 379 379]] = face rectangle start in the upper left corner(column=157,row=84)\
                    # and has the width=379 and height=379

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))   # resizes the image to a third (1/3) of its size;
                                                                    # img.shape[1]/3 = width/3; img.shape[0]/3 = height/3

#cv2.imshow("Gray",gray_img)
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
