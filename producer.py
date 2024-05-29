from kafka import KafkaProducer
import json
import time

# Configuration for Kafka Producer
# Получение адреса Kafka из переменной окружения
kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')
topic_name = 'test-topic'        # Replace with your Kafka topic

# Create an instance of the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send a message
message = {"text": "Hello, Consumer!"}
producer.send(topic_name, message)
producer.flush()  # Ensure all messages are sent

print(f"Sent message to topic '{topic_name}': {message}")

# Close the producer connection
producer.close()
