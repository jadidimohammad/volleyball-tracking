from ultralytics import YOLO
import numpy as np
import cv2
from helper import create_video_writer
from collections import deque
def nearest(res,init):
    box = res.xyxy.cpu().numpy().astype('int')
    mean_c13 = np.mean(box[:, [0, 2]], axis=1)
    mean_c24 = np.mean(box[:, [1, 3]], axis=1)
    center = np.stack((mean_c13, mean_c24), axis=1).astype('int')
    distances = np.linalg.norm(center - init, axis=1).astype('int')
    return center[np.argmin(distances)],min(distances),np.argmin(distances)
model = YOLO("best.pt") # model name

cap = cv2.VideoCapture("Volleyball/MVI_2113.MP4") # file name
writer = create_video_writer(cap, "Output6.mp4")  # output file name
dq = deque(maxlen=10)
z=0
while True:
    print(z)
    success, img = cap.read()
    if not success:
        break
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        print(f"dq is {dq}")
        if len(boxes)>1 and z!=0 and len(dq)>0:
            a,b,c=nearest(boxes,dq[0])
            print(a,b,c)
            if b<300:
                boxes=boxes[c]
        for box in boxes:
            if len(dq)>0:
                a,b,c=nearest(box,dq[0])
                print("dis==",b)
                if b>300:
                    continue
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype('int')
            conf=box.conf[0].cpu().numpy()
            if conf > 0.5:
                cv2.circle(img, tuple((int((x1 + x2) / 2), int((y1 + y2) / 2))), 15, (255, 0, 0), 2)
                center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                dq.appendleft(center)
            for i in range(1, len(dq)):
                if dq[i - 1] is None or dq[i] is None:
                    continue
                cv2.line(img, dq[i - 1], dq[i], (0, 0, 255), thickness=5)

    writer.write(img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()