FROM alpine:3.7

RUN apt-get install --no-cache python3 \ python3 get-pip.py

RUN pip install onnxruntime Flask pillow

COPY modelserver /home/modelserver/

CMD python3 /home/modelserver/app.py

EXPOSE 8001