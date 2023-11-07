from kafka import KafkaProducer

producer = KafkaProducer()
for _ in range(100):
    producer.send('python', b'Python is awesome!')
producer.flush()
