import cv2
import numpy as np
from ultralytics import YOLO
from pynput.keyboard import Key, Controller

# Initialize keyboard controller
keyboard = Controller()


# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Load your custom trained YOLOv8 model
model = YOLO('yolov8n.pt')

# Set up video capture from webcam
cap = cv2.VideoCapture(0)  # 0 means default camera, change it if you have multiple cameras

while True:  # Continuous loop for real-time processing
    ret, frame = cap.read()  # Read frame from the camera

    # Run prediction
    results = model.predict(frame)

    # Extract centroids and class IDs
    # Extract centroids and class IDs
    centroids = []
    class_ids = []
    for det in results[0].boxes.xyxy:
        if len(det) == 6:  # Ensure that the detection has 6 values
            x1, y1, x2, y2, conf, cls = det
            centroid = ((x1 + x2) / 2, (y1 + y2) / 2)
            centroids.append(centroid)
            class_ids.append(int(cls))  # Convert class tensor to int

    # Calculate distances if there are at least 2 detections
    if len(centroids) > 1:
        distances = np.full((len(centroids), len(centroids)), np.inf)
        for i, point1 in enumerate(centroids):
            for j, point2 in enumerate(centroids):
                if i != j:
                    distances[i][j] = euclidean_distance(point1, point2)

        # Find the pair with the shortest distance
        i, j = np.unravel_index(distances.argmin(), distances.shape)
        shortest_distance = distances[i][j]

        # Press keys corresponding to the shortest distance pair
        if shortest_distance < 1000:  # Define a threshold distance
            keyboard.press(str(class_ids[i]))  # Press key for object i
            keyboard.release(str(class_ids[i]))
            keyboard.press(str(class_ids[j]))  # Press key for object j
            keyboard.release(str(class_ids[j]))

    # Display the frame with annotations
    annotated_frame = results[0].plot()
    cv2.imshow('YOLOv8 Inference', annotated_frame)
    if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()

