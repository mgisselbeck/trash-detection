from ultralytics import YOLO

# Load a model
model = YOLO("/Users/mattiegisselbeck/Documents/GitHub/trashbot/yolov8x.pt")  # build a new model from scratch

# Use the model
results = model.train(data="/Users/mattiegisselbeck/Documents/GitHub/trashbot/data.yaml", epochs=3)  # train the model