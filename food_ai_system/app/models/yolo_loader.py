from ultralytics import YOLO

_model = None

def load_model():
    global _model
    if _model is None:
        _model = YOLO("yolov8n.pt")  # lightweight model
    return _model
