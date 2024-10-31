!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
!python -m pip install --upgrade pip

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
!python /content/yolov5/train.py --img 416 --batch 16 --epochs 30 --data /content/Road-suitable-speed/training/sign_data.yaml --weights yolov5l.pt --cache
