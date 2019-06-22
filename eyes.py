# libraries
import cv2
import matplotlib as plt
import numpy as np
import keras
from keras.models import load_model

# load model
model=load_model("data/traintemp.h5")

# initialoize camera
cam=cv2.VideoCapture(0)
while(True):
    
#read frame and processing the frame
    val,frame=cam.read()
    frame=frame[:,81:561,:]
    cv2.imshow("CAMERA",frame)
    frame=cv2.resize(frame,(64,64))
    frame=frame.reshape(1,64,64,3)
    
#prediction
    pred=model.predict(frame)
    pred=pred[0]
    pred.tolist()
    m=max(pred)
    if(pred[0]==m):
        print("Rock")
    elif(pred[1]==m):
        print("Paper")
    elif(pred[2]==m):
        print("Scisors")
    
#release video object
    c=cv2.waitKey(1)
    if(c==ord('q')):
        break

cam.release()
cv2.destroyAllWindows()