import cv2
import time
from retinaface import Face_Recognition

img = cv2.imread('./test/data/test1.jpg')

tic = time.time()

resp = Face_Recognition.detect_faces(img)

for face in resp.values():
    score = round(face['score'], 2)
    facial_area = face['facial_area']

    img = cv2.putText(img, str(score), (facial_area[0], facial_area[1]+25), 
                   cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,255), thickness=2)

    img = cv2.rectangle(img, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), color=(255,0,0), thickness=2)

tac = time.time()

print(f'Pass test 1: [time: {tac-tic}]')

cv2.imwrite('./test/out/test1.jpg', img)

####################################################

tic = time.time()

resp = Face_Recognition.detect_faces('./test/data/test1.jpg')

for face in resp.values():
    score = round(face['score'], 2)
    facial_area = face['facial_area']

    img = cv2.putText(img, str(score), (facial_area[0], facial_area[1]+25), 
                   cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,255), thickness=2)

    img = cv2.rectangle(img, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), color=(255,0,0), thickness=2)

tac = time.time()

print(f'Pass test 2: [time: {tac-tic}]')

cv2.imwrite('./test/out/test1.jpg', img)