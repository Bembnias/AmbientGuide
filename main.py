from ultralytics import YOLO
from ultralytics.solutions import distance_calculation
import cv2

model = YOLO("yolov8n.pt")
names = model.model.names

cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Init distance-calculation obj
dist_obj = distance_calculation.DistanceCalculation()
dist_obj.set_args(names=names, view_img=True)

while cap.isOpened():
    success, im0 = cap.read()
    results = model.predict(source=im0, conf=0.5, show=False)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            object_name = model.names[class_id]

            print(f"Wykryte przedmioty: {object_name}, dokładnosc: {confidence:.2f}, "
                  f"pozycja: ({x1:.2f}, {y1:.2f}) - ({x2:.2f}, {y2:.2f})")

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    tracks = model.track(im0, persist=True, show=False)
    im0 = dist_obj.start_process(im0, tracks)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()