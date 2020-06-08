Step 1: Download the model

https://github.com/onnx/models/blob/master/vision/object_detection_segmentation/ssd/model/ssd-10.onnx

Step 2: Build the Dockerfile

docker build -t <NAME> .

Step 3: Run the image

docker run -p 8001:8001 <NAME>
