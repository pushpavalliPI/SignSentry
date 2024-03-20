from ultralytics import YOLO
import cv2
import pyttsx3
import random
import threading
import time

model_path = "best.pt"

model = YOLO(model_path)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("Welcome to SignSentry")
engine.runAndWait()

previous_output = ""
previous_time = time.time()

def get_class(name: str):
    return list(model.names.values()).index(name)

def get_mask(name: str, results):
    return (results[0].boxes.cls == get_class(name))       

def process_image():
    global previous_output
    global previous_time
    
    randNo = random.randint(0, 12)
    path_file = "RS" + str(randNo) + ".jpg"
    img = cv2.imread(path_file)

    results = model.predict(img)
    bboxes = results[0].boxes.xyxy.tolist()

    for bbox in bboxes:
        start_point = (int(bbox[0]), int(bbox[1]))
        end_point = (int(bbox[2]), int(bbox[3]))
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)
        cv2.putText(img, "sign", (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        class_id = results[0].boxes.cls[0]
        id_int = class_id.item()
        class_detect = results[0].names[(int)(id_int)]
        
        current_time = time.time()
        time_difference = current_time - previous_time
        
        if class_detect != previous_output or time_difference >= 2:
            engine.say(class_detect)
            engine.runAndWait()
            previous_output = class_detect
            previous_time = current_time

    cv2.imshow("Bottle Detection", img)
    threading.Timer(3, process_image).start()

process_image()

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()