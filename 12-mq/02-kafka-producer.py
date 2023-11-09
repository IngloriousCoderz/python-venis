from kafka import KafkaProducer

producer = KafkaProducer(api_version=(3, 6, 0))
for _ in range(100):
    producer.send('python', b'Python is awesome!')
producer.flush()
