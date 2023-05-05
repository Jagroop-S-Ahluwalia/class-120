import cv2
import math

video = cv2.VideoCapture('bb3.mp4')

tracker = cv2.TrackerCSRT_create()
# print(tracker)
returned,myimage = video.read()



bbox = cv2.selectROI('tracking',myimage,False)
print("what is the bbox value: ",bbox)

tracker.init(myimage,bbox)

def drawbox(myimage,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

    cv2.rectangle(myimage,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(myimage,'Tracking: ',(330,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

def goaltracker(myimage,bbox):
    #goalpoints
    cv2.circle(myimage,(p1,p2),3,(0,0,250),2)

    #center point
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(myimage,(c1,c2),2,(0,255,0),2)

    distance = math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    print('distance: ',distance)
    newx.append(c1)
    newy.append(c2)

   

    if distance <= 30: 
        cv2.putText(myimage,'goal reached!',(100,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(212,250,0),2)
    
    else:
        for i in range(len(newx)):
            cv2.circle(myimage,(newx[i],newy[i]),2,(255,0,0),2)


newx = []
newy = []


p1,p2 = 520,300

while True:
    dummy,frame = video.read()
    success,bbox = tracker.update(frame)

    if success == True:
        drawbox(frame,bbox)

    else:
        cv2.putText(frame,'lost: ', (330,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

    goaltracker(frame,bbox)
    cv2.imshow('video',frame)

    if cv2.waitKey(0) == 27:
        break

video.release()
cv2.destroyAllWindows()
 