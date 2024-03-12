import cv2
from functions.consts import KNOWN_DISTANCES, KNOWN_WIDTHS, REFERENCE_IMAGES, focal_lengths
from ultralytics import YOLO

# Inicjalizacja modelu YOLO
model = YOLO("yolov8x.pt")
cap = cv2.VideoCapture(0)

# Pomocnicze funkcje
def object_data(model, image_path, object_name):
    """
    Znajduje i oblicza szerokość wybranego obiektu w pikselach na obrazie referencyjnym.

    :param model: Model YOLO.
    :param image_path: Ścieżka do obrazu referencyjnego.
    :param object_name: Nazwa obiektu, którego szerokość ma być mierzona.
    :return: Szerokość obiektu w pikselach na obrazie referencyjnym.
    """
    image = cv2.imread(image_path)
    results = model.predict(source=image, conf=0.35, show=False)
    
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            detected_object_name = model.names[class_id]
            if detected_object_name == object_name:
                return x2 - x1
    return None

def focal_length_finder(measured_distance, real_width, width_in_rf_image):
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value

def distance_finder(focal_length, real_object_width, object_width_in_frame):
    distance = (real_object_width * focal_length) / object_width_in_frame
    return distance

for object_name, image_path in REFERENCE_IMAGES.items():
    image = cv2.imread(image_path)
    width_in_pixels = object_data(model, image_path, object_name)
    if width_in_pixels is not None:
        focal_length = focal_length_finder(KNOWN_DISTANCES[object_name], KNOWN_WIDTHS[object_name], width_in_pixels)
        focal_lengths[object_name] = focal_length


# W głównej pętli
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model.predict(source=frame, conf=0.35, show=True)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            object_name = model.names[class_id]

            if object_name in KNOWN_WIDTHS:
                object_width_in_frame = x2 - x1
                # Sprawdzamy, czy mamy obliczoną ogniskową dla tego obiektu
                if object_name in focal_lengths:
                    distance = distance_finder(focal_lengths[object_name], KNOWN_WIDTHS[object_name], object_width_in_frame)
                    # Rysowanie i wyświetlanie odległości
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f"{object_name}: {distance} cm", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

