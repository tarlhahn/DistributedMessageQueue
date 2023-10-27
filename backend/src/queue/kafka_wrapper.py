import sys
print(sys.path)

from src.queue.message_queue_abc import MessageQueueWrapperABC
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from kafka.errors import KafkaError
import asyncio

class KafkaWrapper(MessageQueueWrapperABC):
    """
    Kafka implementation of the MessageQueueWrapper.
    Uses the aiokafka library to interact with a Kafka cluster.
    """

    def __init__(self, options):
        """Initialize the Kafka producer and set up the consumer."""
        super().__init__(options)
        
    async def start(self):
        """Start the Kafka producer."""
        pass
        
    async def send(self, topic, message):
        """
        Send a message to a Kafka topic.

        Args:
            topic (str): The Kafka topic to send the message to.
            message (str): The message to send.

        Raises:
            KafkaError: If there's an error sending the message.
        """
        pass

    async def receive(self, topic):
        """
        Asynchronously receive messages from a Kafka topic.

        Args:
            topic (str): The Kafka topic to receive messages from.

        Yields:
            str: Received messages.

        Raises:
            KafkaError: If there's an error receiving messages.
        """
        pass

    async def close(self):
        """Close the Kafka producer."""
        pass

