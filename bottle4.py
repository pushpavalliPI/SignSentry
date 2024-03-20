from ultralytics import YOLO
import cv2
import pyttsx3

model_path = "best.pt"  

model = YOLO(model_path)

def get_class(name: str):
        return list(model.names.values()).index(name)

def get_mask(name: str, results):
        return (results[0].boxes.cls == get_class(name))       

cap = cv2.VideoCapture(0)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("Hello guys, Welcome to the SignSentry.")
engine.runAndWait()

while True:
    ret, frame = cap.read()

    results = model.predict(frame)

    #mask_phone = get_mask('person', results)
    bboxes = results[0].boxes.xyxy.tolist()
    #bboxes = results[0].xyxy.tolist()


    if len(bboxes) > 0:
        print("Sign detected")
        for bbox in bboxes:
                start_point = (int(bbox[0]), int(bbox[1]))
                end_point = (int(bbox[2]), int(bbox[3]))
                cv2.rectangle(frame, start_point, end_point, (255, 0, 0), 2)

                cv2.putText(frame, str("sign"), (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

                class_id = results[0].boxes.cls[0]
                id_int = class_id.item()
                print(results[0].names[(int)(id_int)])

                class_detect = results[0].names[(int)(id_int)]
                engine.say(class_detect)

                #engine.say("Sign detected")
                engine.runAndWait()

    cv2.imshow("Bottle Detection", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
