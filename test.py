from ultralytics import YOLO

model = YOLO("/Users/mattiegisselbeck/Documents/GitHub/trashbot/runs/detect/train5/weights/best.pt") 

results = model("/Users/mattiegisselbeck/Desktop/000013.JPG")  # Predict (Test)
