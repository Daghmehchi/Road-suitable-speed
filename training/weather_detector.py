from roboflow import Roboflow
rf = Roboflow(api_key="**********************")
project = rf.workspace("carlisence-gpfkw").project("weather_detection-v7zbi")
version = project.version(1)
dataset = version.download("folder")

%cd {HOME}
!git clone github.com/ultralytics/ultralytics
%cd {HOME}/ultralytics
!pip install -e .

#free space
from IPython import display
display.clear_output()

#check requerments
import ultralytics
ultralytics.checks()

from ultralytics import YOLO
from IPython.display import display, Image

# train order
!yolo task=classify mode=train model=yolov8n-cls.pt data=/content/Weather_detection-1 epochs=50 imgsz=640
