from kafka import KafkaConsumer

consumer = KafkaConsumer('python', api_version=(
    3, 6, 0))
for message in consumer:
    print(message.topic, ':', message.value.decode())
