import cv2
from functions.ivona import ivona, ivona_color
from functions.detect_color import determine_traffic_light_color
def object_detection(cap, model, engine):
    ret, frame = cap.read()
    results = model.predict(source=frame, conf=0.35, show=True)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            object_name = model.names[class_id]

            print(f"Detected object: {object_name}, confidence: {confidence*100:.2f}%, "f"coordinates: ({x1:.2f}, {y1:.2f}) - ({x2:.2f}, {y2:.2f})")

            if object_name == 'traffic light':  # Adjust this to the traffic light class name
                traffic_light_image = frame[int(y1):int(y2), int(x1):int(x2)]
                traffic_light_color = determine_traffic_light_color(traffic_light_image)
                print(f"The traffic light color is: {traffic_light_color}")
                ivona_color(confidence, x1, x2, frame, object_name, engine, traffic_light_color)
            else:
                ivona(confidence, x1, x2, frame, object_name, engine)