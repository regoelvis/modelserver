# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:16:53 2020

@author: elvis
"""

from flask import Flask
from flask import request
import onnxruntime
from PIL import Image
import io

from utils import utils

app =  Flask(__name__)

model = []

''' Load the .onnx model and set CUDA as the provider if available'''
session=onnxruntime.InferenceSession("model/ssd.onnx")
#session.set_providers(['CUDAExecutionProvider'])
print('Model Loaded')
    
@app.route('/')
def Helloworld():
    return "Server is Running"

@app.route('/predict',methods = ['POST'])
def predict():
    img = Image.open(io.BytesIO(request.data))
    image_size = img.size
    img = img.resize((1200,1200),Image.BILINEAR)
    img = utils.PreProcessImage(img)
    
    result = session.run([],{"image": img})
    response = utils.PostProcess(result, image_size)
    
    return response
    
@app.route('/predictweb',methods = ['POST'])
def predictweb():
    #print(request.data)
    img = Image.open(io.BytesIO(request.data))
    print(img.size)
    #img.show()
    #img.save('img.png')
    img = img.convert('RGB')
    image_size = img.size
    img = img.resize((1200,1200),Image.BILINEAR)
    img = utils.PreProcessImage(img)
    
    result = session.run([],{"image": img})
    response = utils.PostProcess(result, image_size)
    
    return response

@app.route('/predictAndroid',methods = ['POST'])
def predictAndroid():
    #print(request.data)
    img = Image.open(io.BytesIO(request.data))
    print(img.size)
    #img.show()
    img.save('img.png')
    #img = img.convert('RGB')
    image_size = img.size
    img = img.resize((1200,1200),Image.BILINEAR)
    img = utils.PreProcessImage(img)
    
    result = session.run([],{"image": img})
    response = utils.PostProcess(result, image_size)
    
    return response
    
@app.route('/predictdesktop',methods = ['POST'])
def predictdesktop():
    print(len( request.data))
    img = Image.open(io.BytesIO(request.data))
    print(img.size)
    #img.show()
    #img.save('img.png')
    
    img = img.convert('RGB')
    image_size = img.size
    img = img.resize((1200,1200),Image.BILINEAR)
    img = utils.PreProcessImage(img)
    
    result = session.run([],{"image": img})
    response = utils.PostProcess(result, image_size)
    
    return response  

if __name__=='__main__':
    app.run(host = '0.0.0.0',port= 8001)