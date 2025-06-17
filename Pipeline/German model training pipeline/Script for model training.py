# Script for model training

from ultralytics import YOLO
model = YOLO("#␣path␣to␣yolov8l.pt")
model.train(
data="path␣to␣data.yaml",
epochs=100,
imgsz=416,
batch=2,
device="0" # "0" for GPU
)