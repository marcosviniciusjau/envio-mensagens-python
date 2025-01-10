import pika
import json

class RabbitMQPubisher:
  def __init__(self):
    self.__host = "localhost"
    self.__port = 5672
    self.__username= "guest"
    self.__password= "guest"
    self.__exchange= "minha exchange"
    self.__routing_key= ""
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
    return channel
  
  def send_message(self,body: dict): 
    self.__channel.basic_publish(
      exchange=self.__exchange,
      routing_key=self.__routing_key,
      body=json.dumps(body),
      properties= pika.BasicProperties(
        delivery_mode=2
      )
    )
  
rabbit_mq = RabbitMQPubisher()
rabbit_mq.send_message({"msg":"outra mensagem de teste"})