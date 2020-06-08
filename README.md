# modelserver

Modelserver for ssd using Flask and gunicorn

Step 1: Download the ssd.onnx model from ONNX Model Zoo

https://github.com/onnx/models/blob/master/vision/object_detection_segmentation/ssd/model/ssd-10.onnx

Step 2: Place it in the same directory as the source files

Step 3: Start the server with gunicorn

gunicorn wsgi:app
