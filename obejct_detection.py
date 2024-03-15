import cv2
from estimate_distance import estimate_distances

def object_detection(cap, model, f):
    ret, frame = cap.read()
    results = model.predict(source=frame, conf=0.35, show=True)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            object_name = model.names[class_id]
            x0 = abs(x2 - x1)
            y0 = abs(y2 - y1)
            print(f"Detected object: {object_name}, confidence: {confidence*100:.2f}%, "f"coordinates: ({x1:.2f}, {y1:.2f}) - ({x2:.2f}, {y2:.2f})")
            estimate_distances(f, class_id, x0, y0)
