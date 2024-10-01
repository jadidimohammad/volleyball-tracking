# volleyball tracking
All models were trained on 2 * T4

| Model | Precision | Recall |
| ----------- | ----------- | -
| YOLOv11n | 92.8 | 80.4

| Model | Precision | Recall |
| ----------- | ----------- | -
| YOLOv8s | 93.8 | 86.2

### argument
Epoch=100  
batch=16  
optimizer=SGD  
lr=0.01  
momentum=0.937 

## dataset
dataset: Volleyvision  
train set: ~17000 images

## requirement
- ultralytics>=8.3
- numpy
- torch
- collections

## output
![volleyball tracking](image.jpg)
