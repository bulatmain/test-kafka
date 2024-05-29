# Используем базовый образ Python
FROM python:3.9-slim

# Установим зависимости
RUN pip install kafka-python

# Скопируем скрипт consumer в образ
COPY consumer.py /app/consumer.py

# Установим рабочую директорию
WORKDIR /app

# Запустим consumer
CMD ["python", "consumer.py"]
