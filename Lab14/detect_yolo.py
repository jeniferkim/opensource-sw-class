import cv2
import numpy as np

# read image
img = cv2.imread('./Lab14_photo.jpg')  # 내 사진 (HEIC -> JPG 변환본)
if img is None:
    raise SystemExit('이미지를 못 읽음: 파일 이름/경로 확인')
# 폰 사진(5712x4284)은 너무 커서 화면/글자 크기에 맞게 폭 1200px로 줄임
scale = 1200 / img.shape[1]
img = cv2.resize(img, None, fx=scale, fy=scale)
height, width, channel = img.shape
print('original image shape:', height, width, channel)

# get blob from image
blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
print('blob shape:', blob.shape)

# read coco object names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

print('number of classes =', len(classes))

# load pre-trained yolo model from configuration and weight files
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

# set output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
print('output layers:', output_layers)

# detect objects
net.setInput(blob)
outs = net.forward(output_layers)

# get bounding boxes and confidence socres
class_ids = []
confidence_scores = []
boxes = []

for out in outs: # for each detected object

    for detection in out: # for each bounding box

        scores = detection[5:] # scores (confidence) for all classes
        class_id = np.argmax(scores) # class id with the maximum score (confidence)
        confidence = scores[class_id] # the maximum score

        if confidence > 0.3:  # 0.5 -> 0.3: 펼쳐진 교재(book 0.39)까지 잡히도록 낮춤
            # bounding box coordinates
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidence_scores.append(float(confidence))
            class_ids.append(class_id)

print('number of dectected objects =', len(boxes))

# non maximum suppression
# score 임계값도 0.5 -> 0.3 (위 confidence와 맞춤), 0.4 = 겹친 박스 정리 기준
indices = cv2.dnn.NMSBoxes(boxes, confidence_scores, 0.3, 0.4)
print('number of final objects =', len(indices))

# draw bounding boxes with labels on image
colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN

for i in range(len(boxes)):
    if i in indices:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        print(f'class {label} detected at {x}, {y}, {w}, {h}')
        # 원래 colors[i]: 박스가 80개 넘으면 IndexError -> 클래스 번호로 색 고르기
        color = colors[class_ids[i]]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
        cv2.putText(img, f'{label} {confidence_scores[i]:.2f}', (x, max(y - 10, 20)),
                    font, 2, color, 2)

cv2.imwrite('./result.jpg', img)
cv2.imshow('Objects', img)
cv2.waitKey()
cv2.destroyAllWindows()
