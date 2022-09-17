import cv2
from retinaface import Face_Recognition
from retinaface.commons.preprocess import preprocess_image
from threading import Thread

model = Face_Recognition.build_model()

cam = cv2.VideoCapture(0)

loop = 0

def predict(img):
    print(Face_Recognition.verify_database(img))

while True:
    _, frame = cam.read()
    
    cv2.imshow('', frame)

    if loop == 60:
        loop = 0

        p = Thread(target=predict, args=(frame,))

        p.start()
    else:
        loop += 1

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cam.release()
cv2.destroyAllWindows()