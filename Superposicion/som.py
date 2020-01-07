import cv2
 
 
def main():
     
    cap = cv2.VideoCapture(0)
    mog2 = cv2.createBackgroundSubtractorMOG2()
    cv2.BackgroundSubtractorMOG2.setDetectShadows(mog2,False)
 
     
    while(cap.isOpened()):
         
        ret, original = cap.read()
        mask = mog2.apply(original)        
        mask = cv2.erode (mask,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations = 2)
         
        cv2.imshow('Original',original)
        cv2.imshow('Mask',mask)
         
        k = cv2.waitKey(25) & 0xff
        if k == 27:
            break
         
    cap.release()
    cv2.destroyAllWindows()
 
main()