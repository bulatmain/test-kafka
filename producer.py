from kafka import KafkaProducer
import json
import time
import os
from time import sleep

print('producer!')

# Configuration for Kafka Producer
# kafka_bootstrap_server = os.environ.get('KAFKA_BOOTSTRAP_SERVER')
kafka_bootstrap_server = 'my-cluster-kafka-bootstrap:9092'
topic_name = 'test-topic'        # Replace with your Kafka topic

# Create an instance of the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_server,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producer launched!")

i = 0
while True:
    # Send a message
    print(f"Sending message {i}...")
    message = {f"Message {i}": "Hello, Consumer!"}
    producer.send(topic_name, message)
    producer.flush()  # Ensure all messages are sent
    print(f"Sent message to topic '{topic_name}': {message}")
    sleep(1)
    i += 1

# Close the producer connection
producer.close()
