from ultralytics import YOLO
import cv2

# Define the model path and class index for "bottle"
model_path = "yolov8n.pt"  # Replace with your model path
 
# Initialize the YOLO model
model = YOLO(model_path)

def get_class(name: str):
        return list(model.names.values()).index(name)

def get_mask(name: str, results):
        return (results[0].boxes.cls == get_class(name))       

# Start video capture from webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Run inference on the frame
    results = model.predict(frame)

    mask_phone = get_mask('person', results)
    bboxes = results[0].boxes[mask_phone].xyxy.tolist()
    #bboxes = results[0].xyxy.tolist()

    # Loop through detected objects

    if len(bboxes) > 0:
        print("Person detected")
        for bbox in bboxes:
                start_point = (int(bbox[0]), int(bbox[1]))
                end_point = (int(bbox[2]), int(bbox[3]))
                cv2.rectangle(frame, start_point, end_point, (255, 0, 0), 2)

                cv2.putText(frame, str("person"), (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    # Display the frame with detections
    cv2.imshow("Bottle Detection", frame)

    # Exit loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
