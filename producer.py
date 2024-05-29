import os
import json
import time
from kafka import KafkaProducer
 
# Получение адреса Kafka из переменной окружения
kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')

if not kafka_bootstrap_server:
    raise ValueError("KAFKA_BOOTSTRAP_SERVER environment variable not set")

# Настройка Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=[kafka_bootstrap_server],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Отправка сообщений каждые две секунды
topic = 'test_topic'
while True:
    message = {'key': 'value'}
    future = producer.send(topic, value=message)
    try:
        record_metadata = future.get(timeout=10)
        print(f"Message delivered to {record_metadata.topic} [{record_metadata.partition}]")
    except Exception as e:
        print(f"Message delivery failed: {e}")
    time.sleep(2)
