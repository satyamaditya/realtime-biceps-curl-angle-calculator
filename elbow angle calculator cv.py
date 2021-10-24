'''its ADITYA JHA,
in this project i detected angle between wrist & shoulder while center were elbow, with the help of
Computer Vision & google latest library Mediapipe.
its might be good initiative, my vision is to made a application where we dont need GYM TRAINER.
Computer can tell & judge your posture while doing exercise by their angles. and rectify our pose
while we are doing exercise'''


import cv2                          # pip install computer-vision
import mediapipe as mp              # pip install mediapipe
import numpy as np




mppose=mp.solutions.pose
pose=mppose.Pose()
mpdraw=mp.solutions.drawing_utils

for lam in mppose.PoseLandmark:
    print(lam)

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(930,660))
    frame=cv2.flip(frame,1)
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=pose.process(frame1)

    #extract landmarks
    try:
        landmarks=result.pose_landmarks.landmark
        # print(landmarks[13])

        # get coordinates

        shoulder=[landmarks[mppose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mppose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow=[landmarks[mppose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mppose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist=[landmarks[mppose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mppose.PoseLandmark.LEFT_WRIST.value].y]


        # calculate angle:

        a = np.array(shoulder)  # 1st pt
        b = np.array(elbow)  # mid pt
        c = np.array(wrist)  # end pt
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        angle=int(angle)


        #visualize:
        cv2.putText(frame,str(angle),tuple(np.multiply(elbow,[975,650]).astype(int)),cv2.FONT_ITALIC,1,(0,0,0),3)


    except:
        pass

    mpdraw.draw_landmarks(frame,result.pose_landmarks,mppose.POSE_CONNECTIONS)



    cv2.imshow('kush',frame)
    if cv2.waitKey(1)==ord('q'):
        break
