import cv2
from ultralytics import YOLO
from obejct_detection import object_detection

model = YOLO("yolov8x.pt")
cap = cv2.VideoCapture(0)
#f = float(input("Podaj ogniskową kamery w pixelach: "))
f = 1000
while True:
    object_detection(cap, model, f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
