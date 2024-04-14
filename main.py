import cv2
from ultralytics import YOLO
import obejct_detection
from connection import check_device_availability
import threading


print("Starting AmbientGuide")
model = YOLO("yolov8x.pt")
cap = cv2.VideoCapture(0)
f = 1000

thread1 = threading.Thread(target=check_device_availability)
thread2 = threading.Thread(target=obejct_detection.object_detection, args=(cap, model, f))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

cap.release()
cv2.destroyAllWindows()

