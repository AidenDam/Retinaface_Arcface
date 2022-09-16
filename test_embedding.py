import cv2
import time
from retinaface import Face_Recognition

img = cv2.imread('./test/data/test1.jpg')

tic = time.time()

resp = Face_Recognition.represent(img)

tac = time.time()

assert resp != None, 'Error emdedding'

print(f'Pass test 1: [time: {tac-tic}]')

#######################################

tic = time.time()

resp = Face_Recognition.represent('./test/data/test1.jpg')

tac = time.time()

assert resp != None, 'Error emdedding'

print(f'Pass test 1: [time: {tac-tic}]')