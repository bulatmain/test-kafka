# Используем базовый образ Python
FROM python:3.9-slim

# Установим зависимости
RUN pip install kafka-python

# Скопируем скрипт producer в образ
COPY producer.py /app/producer.py

# Установим рабочую директорию
WORKDIR /app

# Запустим producer
CMD ["python", "producer.py"]
