# volleyball tracking
All models were trained on 2 * T4

| Model | Precision | Recall |
| ----------- | ----------- | -
| YOLOv8n | 92.5 | **81.4**
| YOLOv9t | 92.2 | 80.8
| YOLOv10n | **93.3** | 78.9
| YOLOv11n | 92.8 | 80.4
| YOLOv12n | 92.4 | 79.2

| Model | Precision | Recall |
| ----------- | ----------- | -
| YOLOv8s | **94.3** | **85.7**
| YOLOv9s | 93.7 | 84.3
| YOLOv10s | 93.1 | 84.1
| YOLOv11s | 93 | 85.2
| YOLOv12s | 94 | 82.9

| Model | Precision | Recall |
| ----------- | ----------- | -
| [YOLOv8m](https://mega.nz/file/wiFzXZKR#D-xDYEzQur58hdaqn5OzE3b4gY9dSv6UmAyV8YhGcPo) | 93.7 | **87.4**
| [YOLOv11m](https://mega.nz/file/tn0xDJRb#R98AHkamTlCNqhXYAzS3BOS9BlAkLwQTDbv7mhpUH_k) | **94.5** | 87.2

### argument
Epoch=100  
batch=16  
optimizer=SGD  
lr=0.01  
momentum=0.937 

## dataset
dataset: Volleyvision  
train set: ~17000 images  
validation set: ~5000 images

## requirement
- ultralytics>=8.3
- numpy
- torch
- collections

## output
![volleyball tracking](image.jpg)
