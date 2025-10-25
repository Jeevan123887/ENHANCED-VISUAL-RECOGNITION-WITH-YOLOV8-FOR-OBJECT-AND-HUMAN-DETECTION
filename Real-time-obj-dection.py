from ultralytics import YOLO
from enum import Enum
import torch
class ModelType(Enum):
    YOLOv8n = "yolov8n.pt"   # Nano (fastest, least accurate)
    YOLOv8s = "yolov8s.pt"   # Small (balance)
    YOLOv8x = "yolov8x.pt"   # Extra Large (slowest, most accurate)


class Camera(Enum):
    LAPTOP = 0       # Default laptop webcam
    LOGI_1 = 1       # First external webcam
    LOGI_2 = 2       # Second external webcam


def liveObjDetection(modelType: ModelType, camera: Camera):
    print(f"\n Loading model: {modelType.value}")
    model = YOLO(modelType.value)
    
    # Check if GPU is available
    if torch.cuda.is_available():
        print("Using GPU (CUDA) for faster inference")
    else:
       # CUDA (Compute Unified Device Architecture) it is developed by NVIDIA for parallel computing on GPUs.
        print("Using CPU (slower). Consider installing CUDA for GPU acceleration.") 
    # Run real-time object detection with FPS optimizations
    model.track(
        source=camera.value,   # Camera source
        show=True,             # Show video window
        conf=0.5,              # Confidence threshold
        imgsz=416,             # Smaller input size for faster FPS (320 or 416 is smooth)
        vid_stride=2,          # Skip every 2nd frame for speed-up
        persist=True           # Keep track IDs between frames
    )


# ------------------ MAIN ------------------
if __name__ == "__main__":
    # Change model & camera here 
    liveObjDetection(ModelType.YOLOv8n, Camera.LAPTOP)
    # liveObjDetection(ModelType.YOLOv8s, Camera.LOGI_1)
    #liveObjDetection(ModelType.YOLOv8x, Camera.LOGI_2)
