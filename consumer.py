from kafka import KafkaConsumer
import json
import os

print('consumer!')

# Configuration for Kafka Consumer
# kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')
kafka_bootstrap_server = 'broker:9092'
topic_name = 'test-topic'        # Replace with your Kafka topic

# Create an instance of the Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers=[kafka_bootstrap_server],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

consumer.subscribe(topic_name)

print('Consumer launched!')

while True:
    data = next(consumer)
    print(data, data.value)

# Process messages
for message in consumer:
    print(f"Received message from topic '{message.topic}': {message.value}")
