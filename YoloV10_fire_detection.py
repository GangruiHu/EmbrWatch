import cv2
from huggingface_hub import hf_hub_download
from ultralytics import YOLO

print("Downloading model from Hugging Face...")
model_path = hf_hub_download(
    repo_id="TommyNgx/YOLOv10-Fire-and-Smoke-Detection", 
    filename="pytorch_model.bin"
)
print(f"Model loaded from local path: {model_path}")

model = YOLO(model_path)  

# 3. Initialize the webcam stream
# '0' is usually the built-in webcam. Change to '1' for an external USB camera.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting live fire detection feed... Press 'q' to quit.")

while True:
  
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    results = model.predict(frame, conf=0.25, iou=0.45, stream=True)

    for r in results:
        
        annotated_frame = r.plot()

        cv2.imshow("YOLO Fire Detection Live Feed", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Live stream stopped successfully.")
