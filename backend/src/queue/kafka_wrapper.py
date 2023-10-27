import sys

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
        self.bootstrap_servers = f"{options.host}:{options.port}"

    async def start(self):
        """Start the Kafka producer."""
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await self.producer.start()

    async def send(self, topic, message):
        """
        Send a message to a Kafka topic.

        Args:
            topic (str): The Kafka topic to send the message to.
            message (str): The message to send.

        Raises:
            KafkaError: If there's an error sending the message.
        """
        try:
            await self.producer.send_and_wait(topic, message)
        except KafkaError as e:
            print(f"Error sending message to Kafka: {e}")
            raise

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
        consumer = AIOKafkaConsumer(topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',  # start reading at the earliest offset
            enable_auto_commit=False,  # do not commit offsets for fetched messages
        )
        await consumer.start()
        try:
            # Set a timeout for the message poll
            poll_timeout_ms = 2000  # e.g., 5 seconds
        
            # Try to get the next message within the timeout period
            result = await consumer.getmany(timeout_ms=poll_timeout_ms, max_records=100)
            
            # Check if we got a message
            if any(result):
                for tp, messages in result.items():
                    for message in messages:
                        yield message.value
            else:
                # If no message, break the loop
                print("No more messages, exiting...")
        except KafkaError as e:
            print(f"Error receiving message from Kafka: {e}")
            raise
        finally:
            await consumer.stop()

    async def close(self):
        """Close the Kafka producer."""
        await self.producer.stop()

