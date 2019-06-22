#Libraries
import cv2
import numpy as np
import os
import time

#Generator
#Modify or change the following lines of code for a category
"""
Category Template:
    elif c==ord(''):
        f=open("data/",'r')
        i=int(f.read())
        f.close()
        t=str(i)+'.jpg'
        cv2.imwrite(os.path.join("data/",t),frame)
        f=open("data/",'w')
        f.write("%d"%(i+1))
        f.close()
"""

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    frame=frame[:,81:561,:]
    cv2.imshow("CAMERA",frame)
    frame=cv2.resize(frame,(64,64))
    c=cv2.waitKey(1)
    if c==ord('r'):
        f=open("data/rock/rock.txt",'r')
        i=int(f.read())
        f.close()
        t=str(i)+'.jpg'
        cv2.imwrite(os.path.join("data/rock",t),frame)
        f=open("data/rock/rock.txt",'w')
        f.write("%d"%(i+1))
        f.close()
    elif c==ord('p'):
        f=open("data/paper/paper.txt",'r')
        i=int(f.read())
        f.close()
        t=str(i)+'.jpg'
        cv2.imwrite(os.path.join("data/paper",t),frame)
        f=open("data/paper/paper.txt",'w')
        f.write("%d"%(i+1))
        f.close()
    elif c==ord('s'):
        f=open("data/scissors/scissors.txt",'r')
        i=int(f.read())
        f.close()
        t=str(i)+'.jpg'
        cv2.imwrite(os.path.join("data/scissors",t),frame)
        f=open("data/scissors/scissors.txt",'w')
        f.write("%d"%(i+1))
        f.close()
    elif c==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()