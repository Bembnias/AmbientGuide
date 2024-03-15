from estimate_distance import estimate_distances
from object_prioritization import object_prioritization
def object_detection(cap, model, f):
    ret, frame = cap.read()
    results = model.predict(source=frame, conf=0.35, show=True)
    distance = []
    row = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            x0 = abs(x2 - x1)
            y0 = abs(y2 - y1)
            d = estimate_distances(f, class_id, x0, y0)
            row.append(class_id)
            row.append(d)
        if row:
            distance.append(row)
            row = []
    priority = object_prioritization(distance)
    for object in priority:
        object_name = model.names[object[0]]
        print(f"Detected object: {object_name}")
