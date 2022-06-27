FROM python:alpine

RUN mkdir app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV TZ=Europe/Moscow

ENTRYPOINT [ "python", "app.py" ]

CMD []