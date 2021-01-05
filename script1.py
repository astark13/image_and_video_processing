import cv2

img=cv2.imread("galaxy.jpg",0)                # 1 = colored image; 0 = black and white image; -1 = colore with transparency 

print(type(img))
print(img)                 # display the array that represents the image
print(img.shape)
print(img.ndim)

#cv2.imshow("Galaxy",img)
#resized_image=cv2.resize(img,(500,1000))      # (500,1000) = (width,height) resizees the picture to the give pixel size
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))      # img.shape[1]/2 = reduces in half the width of the picture;
                                                                             # [1] is the second element of the tuple shown by "print(img)"
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)      # saves the resized image, with a new name, in the current location
cv2.waitKey(2000)           # if the value is "0" the image disappears when you push the "enter" button
cv2.destroyAllWindows()     #after displaying the image for 2000miliseconds, the image is closed  