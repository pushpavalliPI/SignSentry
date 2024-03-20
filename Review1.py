""" from ultralytics import YOLO
import cv2
import pyttsx3
import random
import time

# Define the model path and class index for "bottle"
#model_path = "yolov8n.pt"  # Replace with your model path

model_path = "C:/Users/Rohii/Downloads/best.pt"

# Initialize the YOLO model
model = YOLO(model_path)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("Welcome to the Navigation assistant.")
engine.runAndWait()

def get_class(name: str):
        return list(model.names.values()).index(name)

def get_mask(name: str, results):
        return (results[0].boxes.cls == get_class(name))       

# Start video capture from webcam

t_end = time.time() + 60*3

while time.time() < t_end:

        randNo = random.randint(0,15)
        img = cv2.imread("C:/Users/Rohii/Desktop/My_VSCode/AllPython/RS" + (str)(randNo) +".jpg")
        # cap = cv2.VideoCapture(0)

        while True:
        # Capture a frame from the webcam

        #     ret, frame = cap.read()

        # Run inference on the frame
                results = model.predict(img)

                #     mask_phone = get_mask('person', results)
                bboxes = results[0].boxes.xyxy.tolist()

                # Loop through detected objects
                for bbox in bboxes:

                        start_point = (int(bbox[0]), int(bbox[1]))
                        end_point = (int(bbox[2]), int(bbox[3]))
                        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)

                        cv2.putText(img, str("sign"), (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

                        engine.say("Sign detected")
                        engine.runAndWait()
                        engine.stop()
        # Display the frame with detections
                cv2.imshow("Bottle Detection", img)

        # Exit loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

# Release resources
# cap.release()
cv2.destroyAllWindows()

 """



from ultralytics import YOLO
import cv2
import pyttsx3
import random
import threading


model_path = "C:/Users/Rohii/Downloads/best.pt"


model = YOLO(model_path)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("Hello guys, Welcome to the SignSentry.")
engine.runAndWait()

def get_class(name: str):
    return list(model.names.values()).index(name)

def get_mask(name: str, results):
    return (results[0].boxes.cls == get_class(name))       

def process_image():
    randNo = random.randint(0, 15)
    img = cv2.imread("C:/Users/Rohii/Desktop/My_VSCode/AllPython/RS" + str(randNo) + ".jpg")

    results = model.predict(img)
    #print(results)
    bboxes = results[0].boxes.xyxy.tolist()

    for bbox in bboxes:
        start_point = (int(bbox[0]), int(bbox[1]))
        end_point = (int(bbox[2]), int(bbox[3]))
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)

        cv2.putText(img, "sign", (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        engine.say("Sign detected")
        engine.runAndWait()
        #engine.stop()

    cv2.imshow("Bottle Detection", img)

    threading.Timer(2, process_image).start()

process_image()

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()