

 # Object detection  (  Vehicle Number Plate Detection )-----------------------------------------

from ultralytics import YOLO v8

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=30)  # train the model


