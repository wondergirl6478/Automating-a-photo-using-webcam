import cv2  

def take_snapshot():

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result = False


    videoCaptureObject.release()

    cv2.destroyAllWindows()

take_snapshot()