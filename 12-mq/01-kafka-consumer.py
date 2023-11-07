from kafka import KafkaConsumer

consumer = KafkaConsumer('python')
for message in consumer:
    print(message.topic, ':', message.value.decode())
