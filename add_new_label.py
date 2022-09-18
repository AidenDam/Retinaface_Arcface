import os
import argparse
from retinaface import Face_Recognition

def add_new_embdedding(label:str, img):
    with open('databas.txt', 'r') as f:
        while True:
            line = f.readline()
            if label == line.split()[0]:
                raise 'Label already exists!'
            if not line:
                break

    resp = Face_Recognition.represent(img)

    with open('databas.txt', 'a') as f:
        f.writelines(label + ' ' + ' '.join([str(i) for i in resp]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store', default=None, type=str, help='Label of imae')
    parser.add_argument('-f', action='store', default=None, type=str, help='Path to image.')
    args = parser.parse_args()

    if args.f:
        path = args.f
    else:
        path = input('Enter path of image: ').strip()

    assert os.path.exists(path), 'Path not match.'
    assert path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')), 'File is not image.'

    if args.l:
        label = args.l
    else:
        label = input('Enter label of image: ').strip()

    label = label.replace(' ', '_')

    # add_new_embdedding(label, path)

    print('Add successful.')