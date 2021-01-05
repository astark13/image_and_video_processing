import cv2, time

video=cv2.VideoCapture(0, cv2.CAP_DSHOW)    # captures image from webcam 0; if there are multiple webcams\
                                            # you can specify which webcam's image to capture (0, 1, 2,...)
                                            # !!! This turns on the camera!!!

a=0

while True:
    a=a+1
    check, frame = video.read()   # "check" is a boolean variable that has the value TRUE if the video is running

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",gray)   # displays the images/video from the camera in gray scale

    key=cv2.waitKey(1)             # Waits 1 milisecond until it shows the next frame; basically a video

    if key==ord('q'):              # press "q" to quit
        break

print(a)                        # total number of frames in the video
video.release()                 # !!!This turns off the camera!!!
cv2.destroyAllWindows()  