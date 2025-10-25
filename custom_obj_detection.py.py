from ultralytics import YOLO
from enum import Enum
import torch

class ModelType(Enum):
    YOLOv8n = "yolov8n.pt"   # Nano (fastest, less accurate)
    YOLOv8s = "yolov8s.pt"   # Small (balance speed & accuracy)
    YOLOv8x = "yolov8x.pt"   # Extra Large (most accurate)

class Camera(Enum):
    LAPTOP = 0       # Default laptop webcam
    LOGI_1 = 1       # First external webcam
    LOGI_2 = 2       # Second external webcam

def liveObjDetection(modelType: ModelType, camera: Camera):
    print(f"\n📡 Loading model: {modelType.value}")
    model = YOLO(modelType.value)  # Pre-trained YOLOv8 model

    if torch.cuda.is_available():
        print("✅ Using GPU (CUDA) for faster inference")
    else:
        print("⚠️ Using CPU (slower).")

    # Run real-time object detection
    model.track(
        source=camera.value,   # Camera source
        show=True,             # Show live video feed
        conf=0.5,              # Confidence threshold
        imgsz=416,             # Image size for speed
        vid_stride=2,          # Skip frames for speed
        persist=True           # Keep track of IDs between frames
    )

# ------------------ MAIN ------------------
if __name__ == "__main__":
    liveObjDetection(ModelType.YOLOv8n, Camera.LAPTOP)
    # liveObjDetection(ModelType.YOLOv8s, Camera.LOGI_1)
    # liveObjDetection(ModelType.YOLOv8x, Camera.LOGI_2)
