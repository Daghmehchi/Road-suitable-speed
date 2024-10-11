%cd /content
!git clone https://github.com/ultralytics/yolov5
%cd yolov5
!pip install -r requirements.txt
!pip install kaggle
!pip install numpy
!python -m pip install --upgrade pip
!pip install torch

# Api for kaggle.json
api_token = {
    "username": "daghmehchi",
    "key": "204cf422231f7a64709979b248e88822"
}

import json
import os

os.makedirs('/root/.kaggle/', exist_ok=True)

with open('/root/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token, file)

# Access permission
os.chmod('/root/.kaggle/kaggle.json', 600)

# download from Kaggle
!kaggle datasets download -d pkdarabi/cardetection

# unzip
!unzip cardetection.zip

# train order
!python train.py --img 416 --batch 16 --epochs 20 --data /content/yolov5/car/data.yaml --weights yolov5s.pt --cache
