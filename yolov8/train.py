from ultralytics import YOLO


model = YOLO('./models/yolov8n-pose.pt')

if __name__ == '__main__':
    results = model.train(data="utils/dataset-pose/data.yaml", epochs=300, imgsz=640, device=0, batch=8)


