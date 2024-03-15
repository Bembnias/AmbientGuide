import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model.predict(source=frame, conf=0.5, show=True)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            object_name = model.names[class_id]

            print(f"Wykryte przedmioty: {object_name}, dokładnosc: {confidence:.2f}, "
                  f"pozycja: ({x1:.2f}, {y1:.2f}) - ({x2:.2f}, {y2:.2f})")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()