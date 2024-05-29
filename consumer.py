from kafka import KafkaConsumer
import json
import os

# Configuration for Kafka Consumer
kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')
topic_name = 'test-topic'        # Replace with your Kafka topic

# Create an instance of the Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_bootstrap_server,
    auto_offset_reset='earliest',  # Start from the earliest messages
    enable_auto_commit=True,
    group_id='my-group',           # Consumer group id
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Process messages
for message in consumer:
    print(f"Received message from topic '{message.topic}': {message.value}")

# Clean up: the consumer will continue listening until the program is interrupted or killed.
# In a real-world application, ensure proper shutdown and exception handling.
