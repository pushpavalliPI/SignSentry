from ultralytics import YOLO
import cv2
import pyttsx3
import random
import threading


model_path = "best.pt"

# global prev 
# prev = " "


model = YOLO(model_path)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

engine.say("Welcome to SignSentry")
engine.runAndWait()

# def get_class_name(results):
#   class_id = results[0].boxes.cls[0]
#   class_name = model.names[class_id]
#   return class_name


def get_class(name: str):
    return list(model.names.values()).index(name)

def get_mask(name: str, results):
    return (results[0].boxes.cls == get_class(name))       

def process_image(n: int):
    # randNo = random.randint(0, 12)
    # path_file = "RS" + str(randNo) + ".jpg"
    # path_file = "RS6.jpg"
    path_file = "RS" + str(n) + ".jpg"
    img = cv2.imread(path_file)


    results = model.predict(img)
    bboxes = results[0].boxes.xyxy.tolist()

    i = 0
    for bbox in bboxes:
        start_point = (int(bbox[0]), int(bbox[1]))
        end_point = (int(bbox[2]), int(bbox[3]))
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)

        cv2.putText(img, "sign", (start_point[0], start_point[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        class_id = results[0].boxes.cls[0]
        # print(type(class_id))
        # print(class_id)
        id_int = class_id.item()
        # print(type(id_int))
        # print(results[0].names[(int)(id_int)])
        # print(results)
        #class_name = model.names[class_id]

          

    # class_name = get_class_name(results)
        #print(f"Class name: {class_name}")
        cv2.imshow("Bottle Detection", img)

        class_detect = results[0].names[(int)(id_int)]
        if class_detect != "Traffic_Signal":
            engine.say(class_detect)
            engine.runAndWait()
            engine.stop()

        # global prev

        # if class_detect == prev:
        #     continue
        # else:
        #     #global prev
        #     engine.say(class_detect)
        #     engine.runAndWait()
        #     engine.stop()
        # prev = class_detect

    # i = i+1
    threading.Timer(3, process_image).start()

for n in range (0,7):
    process_image(n)


while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()

