from estimate_distance import estimate_distances
from object_prioritization import object_prioritization
from udp_transfer import send_packet, send_packet_with_color
from detect_side import detect_side
from polish_object import polish_object
from detect_color import determine_traffic_light_color
import time
import connection


def object_detection(cap, model, f):
    while True:
        ip_address = connection.get_IP()
        if ip_address is not None:
            ret, frame = cap.read()
            results = model.predict(source=frame, conf=0.4, show=False)
            distance = []
            row = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    class_id = int(box.cls[0])
                    x0 = abs(x2 - x1)
                    y0 = abs(y2 - y1)
                    d = estimate_distances(f, class_id, x0, y0)
                    row.append(class_id)
                    row.append(d)
                    row.append(x1)
                    row.append(x2)
                if row:
                    distance.append(row)
                    row = []
            priority = object_prioritization(distance)
            for object in priority:
                if(object[1] >=0.25):
                    object_name = model.names[object[0]]
                    polish_name = polish_object(object_name)
                    if object_name == 'traffic light':  # Adjust this to the traffic light class name
                        traffic_light_image = frame[int(y1):int(y2), int(x1):int(x2)]
                        traffic_light_color = determine_traffic_light_color(traffic_light_image)
                        side = detect_side(object[2], object[3], frame)
                        send_packet_with_color(polish_name, side, traffic_light_color)
                        time.sleep(1.5)
                    else:
                        side = detect_side(object[2], object[3], frame)
                        send_packet(polish_name, side)
                        time.sleep(1.5)
