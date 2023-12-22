# Trash Detection Using YOLOv8
Description 

| Model                                                                                | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640                   | 53.9                 | 479.1                          | 3.53                                | 68.2               | 257.8             |
    
<a name="user-content-code"></a>
<h2 id="user-content-code-and-syntax-highlighting"><a class="heading-link" href="#code-and-syntax-highlighting">Installation & Configuration<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p> To install TACO, clone <a href="http://tacodataset.org/" rel="nofollow">TACO</a> repository.</p>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content=" git clone https://github.com/pedropro/TACO"><pre lang="no-highlight" class="notranslate">
<code> git clone https://github.com/pedropro/TACO
</code></pre></div>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="cd yolov5"><pre lang="no-highlight" class="notranslate">
<code> cd yolov5
</code></pre></div>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="pip install -r requirements.txt"><pre lang="no-highlight" class="notranslate">
<code> pip install -r requirements.txt 
</code></pre></div>
<p>2. Create an Anaconda Environment for YOLOv8</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="cd /Users/mattiegisselbeck/yolov5"><pre lang="no-highlight" class="notranslate">
<code> cd /Users/mattiegisselbeck/yolov5
</code></pre></div>

 <div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="conda create --name yolov5 python=3.8"><pre lang="no-highlight" class="notranslate">
<code>conda create --name yolov5 python=3.8
</code></pre></div>

 <a name="user-content-code"></a>
<h2 id="user-content-code-and-syntax-highlighting"><a class="heading-link" href="#code-and-syntax-highlighting">Index<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>

## `/trash-detection`

* trash-detection-yolov8.ipynb: This jupyter notebook contains the components to build and train a trash objection detection model using YOLOv8.

* data.yaml: This .yaml file sets image(s) path and the number of set classes for the TACO dataset (this is used in training the YOLO model). 

* train.py: This .py file builds and trains a custom YOLOv8 model on the TACO dataset when executed in the CLI. 

## `/runs`
### `/detect`
  * `/train`
     * results.csv: This .csv shows the evaluation metrics of custom YOLOv8 model.
     * train_batch*.jpg: These .jpg(s) are visualizations of the trained images. 

         
## `/models`
* trash-detection-yolov8x.pt: This .pt is the custom YOLOv8x model trained off the TACO dataset.
