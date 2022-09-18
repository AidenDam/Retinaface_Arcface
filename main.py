import cv2
from retinaface import Face_Recognition
from retinaface.model import arcface
from threading import Thread, Lock


# threadLimiter = threading.BoundedSemaphore(1)
def predict(img):
    # threadLimiter.acquire()
    # print (threading.currentThread().getName(), 'Starting')
    out = Face_Recognition.verify_database(img, model=model, detector_backend=detector_backend)
    with lock:
        if out != None:
            facial_area[:] = out['facial_area']
        else:
            facial_area[:] = []
    # print(out)
    # print (threading.currentThread().getName(), 'Exiting')
    # threadLimiter.release()

if __name__ == '__main__':
    lock = Lock()
    model = arcface.loadModel()
    detector_backend = Face_Recognition.build_model()
    loop = fps = 60
    facial_area = []
    
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        fame = cv2.flip(frame, 1)

        if loop == fps:
            loop = 0

            p = Thread(target=predict, args=(frame,))

            p.start()
        else:
            loop += 1

        if len(facial_area) == 4:
            frame = cv2.rectangle(frame, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), color=(0,255,0), thickness=1)

        cv2.imshow('', frame)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cam.release()
    cv2.destroyAllWindows()