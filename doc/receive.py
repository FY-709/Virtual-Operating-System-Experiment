import pika
from judge import save
from judge import compile_code
from judge import run_code
import db


parameters = (
    pika.ConnectionParameters(host="localhost")
                              )

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test')
cdb = db.opdb('localhost','root','qwer1234','opdb')

def callback(ch, method, propertites, body):
    body = bytes.decode(body)
    f_name = body[0:32]
    f_detail = body[32:]
    save(f_detail.encode('utf-8'),f_name)
    cdb.init_data(f_name)
    compile_status = compile_code(f_name)
    compile_status[1] = run_code(f_name) 
    cdb.save_result(f_name,compile_status[0],compile_status[1])
    print(" [x] Received {}"+compile_status[1])


channel.basic_consume('test', callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()