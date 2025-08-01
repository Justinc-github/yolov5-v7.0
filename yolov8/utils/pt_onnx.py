from ultralytics import YOLO

# load a pretrained model (recommended for training)
# model = YOLO('C:/Users/Justinc/Desktop/yolov5-v7.0/yolov5-v7.0/runs/train/exp21/weights/best.pt')
model = YOLO('C:/Users/Justinc/Desktop/yolov5-v7.0/yolov5-v7.0/yolov8/runs/pose/train22/weights/best.pt')

# Export the model
success = model.export(format='onnx')

print(success)
