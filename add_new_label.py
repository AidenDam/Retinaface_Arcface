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
    path = './aiden.jpg'

    add_new_embdedding('Dao', path)