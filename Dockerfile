FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN set PYTHONPATH='${PYTHONPATH}:/app'

COPY . .

CMD ["python", "./app.py"]