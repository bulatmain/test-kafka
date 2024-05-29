import os
from kafka import KafkaConsumer

# Получение адреса Kafka из переменной окружения
kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')

if not kafka_bootstrap_server:
    raise ValueError("KAFKA_BOOTSTRAP_SERVER environment variable not set")

# Настройка Kafka Consumer
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers=[kafka_bootstrap_server],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Ha-ha-ha")

# Получение сообщений
for message in consumer:
    print(f"Received message: {message.value}")
