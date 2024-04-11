import cv2
from ultralytics import YOLO
import obejct_detection
from connection import getIP
import threading
from connection_status import udp_receive_send


ip_address = getIP()

if(ip_address != 0):
    thread = threading.Thread(target=udp_receive_send)
    thread.start()

def get_IP():
    return ip_address

model = YOLO("yolov8x.pt")
cap = cv2.VideoCapture(0)
f = 1000
while True:
    obejct_detection.object_detection(cap, model, f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()