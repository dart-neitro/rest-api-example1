FROM python:3-alpine

RUN pip install --upgrade pip
RUN pip install flask

RUN mkdir /app
WORKDIR /app

COPY app.py /app/app.py

CMD ["python", "app.py"]