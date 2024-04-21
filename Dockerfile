FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /assets


COPY image/ma1.png /assets/ma1.png
COPY image/ma2.png /assets/ma2.png
COPY image/ma3.png /assets/ma3.png
COPY image/ma4.png /assets/ma4.png
COPY image/empty.png /assets/empty.png
COPY mama.py /app/mama.py

WORKDIR /app

CMD [ "python", "mama.py" ]