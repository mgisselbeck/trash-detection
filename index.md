# Index

## `/trash-detection`

* trash-detection-yolov8.ipynb: This jupyter notebook contains the components to build and train a trash objection detection model using YOLOv8.

* data.yaml: This .yaml file sets image(s) path and the number of set classes for the TACO dataset (this is used in training the YOLO model). 

* train.py: This .py file builds and trains a custom YOLOv8 model on the TACO dataset when executed in the CLI. 

### `/runs`
* `/detect`
  * `/train`
     * results.csv: This .csv shows the evaluation metrics of custom YOLOv8 model.
     * train_batch*.jpg: These .jpg(s) are visualizations of the trained images. 
     * `/weights`
       * best.pt: 
       * last.pt
         
### `/models`
* yolov8*.yaml: These .yaml files are used for building and training a custom YOLOv8 model. 
* yolov8s.yaml
* yolov8x.yaml
