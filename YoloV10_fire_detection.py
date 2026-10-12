import csv
from datetime import datetime
import os
import cv2
from huggingface_hub import hf_hub_download
import folium
import pandas as pd
from pynmeagps import NMEAReader
import serial
from ultralytics import YOLO

# --- CONFIGURATION ---
GPS_PORT = "COM3"      # Update to your drone GPS module COM port
GPS_BAUD = 9600
VIDEO_SOURCE = 0       # 0 for default webcam or capture card index
LOG_FILE = "drone_targets.csv"
MAP_FILE = "drone_targets_map.html"

# --- 1. INITIALIZE DRONE GPS MODULE ---
print(f"Connecting to drone GPS module on {GPS_PORT}...")
try:
    gps_serial = serial.Serial(GPS_PORT, GPS_BAUD, timeout=0.1)
    gps_enabled = True
    print("GPS module connected successfully.")
except Exception as e:
    print(f"Warning: Could not open GPS port ({e}). Running without GPS tracking.")
    gps_enabled = False

current_lat, current_lon = 0.0, 0.0

def read_gps():
    """Reads the latest NMEA sentence to update latitude and longitude."""
    global current_lat, current_lon
    if not gps_enabled:
        return
    try:
        while gps_serial.in_waiting:
            data = gps_serial.readline()
            nmr = NMEAReader.parse(data.decode("utf-8", errors="ignore"))
            if nmr and nmr.msgID == "GGA":
                if getattr(nmr, "lat", None) and getattr(nmr, "lon", None):
                    current_lat = nmr.lat
                    current_lon = nmr.lon
    except Exception:
        pass

print("Downloading/loading model from Hugging Face...")
model_path = hf_hub_download(
    repo_id="TommyNgx/YOLOv10-Fire-and-Smoke-Detection", 
    filename="pytorch_model.bin"
)
print(f"Model loaded from local path: {model_path}")[cite: 1]

model = YOLO(model_path)[cite: 1]

cap = cv2.VideoCapture(VIDEO_SOURCE)[cite: 1]

if not cap.isOpened():
    print("Error: Could not open video source.")[cite: 1]
    if gps_enabled:
        gps_serial.close()
    exit()

with open(LOG_FILE, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Latitude", "Longitude", "Status"])

print("Starting live drone feed and tracking... Press 'q' to quit.")

while True:

    read_gps()

    ret, frame = cap.read()[cite: 1]
    if not ret:
        print("Failed to grab frame.")[cite: 1]
        break

    results = model.predict(frame, conf=0.25, iou=0.45, stream=True)[cite: 1]

    target_detected = False
    for r in results:
        annotated_frame = r.plot()[cite: 1]
        if len(r.boxes) > 0:
            target_detected = True

        cv2.imshow("Drone Vision - YOLO & M100 GPS Tracker", annotated_frame)[cite: 1]

    if target_detected and gps_enabled:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[TARGET FOUND] Lat: {current_lat}, Lon: {current_lon} at {timestamp}")
        with open(LOG_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, current_lat, current_lon, "Target Detected"])


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()[cite: 1]
if gps_enabled:
    gps_serial.close()
cv2.destroyAllWindows()[cite: 1]
print("Live stream stopped successfully.")[cite: 1]


if os.path.exists(LOG_FILE):
    df = pd.read_csv(LOG_FILE)
    if not df.empty and df["Latitude"].iloc[0] != 0.0:
        print("Generating interactive map...")
        m = folium.Map(location=[df["Latitude"].iloc[0], df["Longitude"].iloc[0]], zoom_start=18)
        for _, row in df.iterrows():
            folium.Marker(
                [row["Latitude"], row["Longitude"]],
                popup=f"Time: {row['Timestamp']}",
                icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
        m.save(MAP_FILE)
        print(f"Map successfully generated and saved as '{MAP_FILE}'!")
    else:
        print("No valid GPS coordinates logged during session to generate map.")