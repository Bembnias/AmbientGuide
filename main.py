import cv2
import pyttsx3
from ultralytics import YOLO
from functions.obejct_detection import object_detection

model = YOLO("yolov8x.pt")
cap = cv2.VideoCapture(0)
engine = pyttsx3.init()

while True:
    object_detection(cap, model, engine)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
