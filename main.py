import mediapipe as mp
import cv2
import time 


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime=0
cTime=0
while True:
    success  , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lms in enumerate(handlms.landmark):
                h,w,c =  img.shape
                cx,cy = int(lms.x*w),int(lms.y*h)
                print(id,cx,cy)
                cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms , mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),3)



    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows() 