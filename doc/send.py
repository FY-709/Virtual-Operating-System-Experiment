import pika


parameters = (
    # pika.ConnectionParameters(host='rabbitmq.zone1.yourdomain.com'),
    # pika.ConnectionParameters(host='rabbitmq.zone2.yourdomain.com',
    #                           connection_attempts=5, retry_delay=1)
    pika.ConnectionParameters(host="localhost")
                              )

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
with open("test1.cpp",'rb') as f:
    code = f.read()
code = b"098f6bcd4621d373cade4e832627b4f6" + code
channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=code
)

print(b"[x] Sent " + code)
connection.close()