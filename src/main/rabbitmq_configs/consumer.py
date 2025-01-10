import pika

def rabbitmq_callback(ch, method, properties, body):
  msg = body.decode("utf-8")
  msg_ok = json_loads(msg)
  print(msg_ok)
class RabbitMQConsumer:
  def __init__(self):
    self.__host = "localhost"
    self.__port = 5672
    self.__username= "guest"
    self.__password= "guest"
    self.__queue= "minha_queue"
    self.__channel =  self.create_channel()
   
  def create_channel(self)->None:
    connection_params = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=pika.PlainCredentials(
        username=self.__username,
        password=self.__password
        ))
    
    channel = pika.BlockingConnection(connection_params).channel()
    channel.queue_declare(queue=self.__queue, durable=True)
    channel.basic_consume(
      queue=self.__queue,
      auto_ack=True,
      on_message_callback=rabbitmq_callback
    )
    return channel
  
  def start(self):
   print("Sistema conectado ao rabbitmq")
   self.__channel.start_consuming()