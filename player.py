from keras.models import load_model
import cv2
import random
import time
import numpy as np

model = load_model("data/traintemp.h5")

cap = cv2.VideoCapture(0)

n = int(input("Enter the number of rounds you want to play : "))
cou = 1
score = [0, 0]
print("\nUser\tComputer")
while True:
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print(0)
    c = random.randint(0, 2)
    predictions = [0, 0, 0]
    for i in range(10):
        ret, frame = cap.read()
        frame = frame[:, 81:561, :]
        frame = cv2.resize(frame, (64, 64))
        frame = frame.reshape(1, 64, 64, 3)
        pred=model.predict(frame)
        pred = pred[0]
        pred.tolist()
        m = max(pred)
        if pred[0] == m:
            predictions[0] += 1
        elif pred[1] == m:
            predictions[0] += 1
        elif pred[2] == m:
            predictions[0] += 1
    m = max(predictions)
    if predictions[0] == m:
        p = 0
    elif predictions[1] == m:
        p = 1
    elif predictions[2] == m:
        p = 2
    print("\b\b\b\b\b\b")
    if p == c:
        print("%d\t%d" % (score[0], score[1]))
    elif p == 0 and c == 1:
        score[1] += 1
        print("%d\t%d" % (score[0], score[1]))
    elif p == 0 and c == 2:
        score[0] += 1
        print("%d\t%d" % (score[0], score[1]))
    elif p == 1 and c == 0:
        score[0] += 1
        print("%d\t%d" % (score[0], score[1]))
    elif p == 1 and c == 2:
        score[1] += 1
        print("%d\t%d" % (score[0], score[1]))
    elif p == 2 and c == 0:
        score[1] += 1
        print("%d\t%d" % (score[0], score[1]))
    elif p == 2 and c == 1:
        score[0] += 1
        print("%d\t%d" % (score[0], score[1]))
    cou += 1
    if cou > n:
        break

cap.release()
if score[0] > score[1]:
    print("USER WINS")
elif score[1] > score[0]:
    print("COMPUTER WINS")
else:
    print("IT\'S A DRAW")