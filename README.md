# RetinaFace and Arcface
This repo implements RetinaFace and Arcface for face detection.

## Preparation
To run it, you need to clone repo and install package:
``` 
git clone https://github.com/AidenDam/Retinaface_Arcface.git
cd Retinaface_Arcface
pip install -r requirements.txt
```

## How to run
- To test the model, run:
``` 
python test_detector.py
python test_embedding.py
python test_compute_distance.py
```

- To add a new face to database.txt:
``` 
python add_new_label.py -f <link img> -l <label>
```

- To run:
```
python main.py
```
- Note: if you don't have gpu, you should config the frame will detect after n frames. by:
```
python main.py -fps <n frames>
```
---
If you have any question or encouter any problem regarding this repo. Please open an issue and cc me. Thank you.
