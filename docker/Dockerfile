FROM python:3.7

WORKDIR /home/

COPY /modelserver/requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY /modelserver /home/

RUN ls

CMD ["gunicorn","--bind", ":8001", "wsgi:app"]

EXPOSE 8001