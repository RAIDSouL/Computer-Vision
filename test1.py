import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# cs = (1280,720)
# ts = (300,300)

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, cs[0])
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cs[1])

while(True):
    ret,im = cap.read()
    # im_sized = cv2.resize(im,ts)
    
    #############################
    im_flipped = cv2.flip(im, 1)
    #############################
    #############################
    L = 25
    kernel = np.ones((L,L), np.float32) / L / L
    imb= cv2.filter2D(im_flipped, -1, kernel)
    cv2.imshow('camera',im_flipped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()