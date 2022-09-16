import time
from retinaface import Face_Recognition

tic = time.time()

dst = Face_Recognition.verify('./test/data/test3.jpg', './test/data/test2.jpg', distance_metric=['cosine', 'euclidean', 'euclidean_l2'])

tac = time.time()

print(f'Pass test 1: [time: {tac-tic} res: {dst}]')

#######################################

tic = time.time()

dst = Face_Recognition.verify([['./test/data/test3.jpg', './test/data/test2.jpg'], ['./test/data/test1.jpg', './test/data/test2.jpg']])

tac = time.time()

print(f'Pass test 2: [time: {tac-tic} res: {dst}]')