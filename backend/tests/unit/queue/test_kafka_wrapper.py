import unittest
from unittest.mock import patch, Mock, AsyncMock
from src.queue.kafka_wrapper import KafkaWrapper

class TestKafkaWrapper(unittest.IsolatedAsyncioTestCase):
    """
    Unit tests for the KafkaWrapper class.
    This class tests the asynchronous methods provided by the KafkaWrapper.
    """

    # Setting up the asynchronous test environment.
    # Mocking the AIOKafkaProducer to simulate Kafka producer behavior.
    @patch('src.queue.kafka_wrapper.AIOKafkaProducer', return_value=AsyncMock()) 
    async def asyncSetUp(self, MockKafkaProducer):
        """
        Asynchronous setup for the test cases.
        Initializes the KafkaWrapper with mock options and starts the connection.
        """
        
        options = Mock()
        options.host = 'localhost'
        options.port = '9092'
        
        self.wrapper = KafkaWrapper(options)
        await self.wrapper.start()

    async def asyncTearDown(self):
        """
        Asynchronous teardown for the test cases.
        Closes the KafkaWrapper connection after each test run.
        """
        await self.wrapper.close()
        
    async def test_send(self):
        """
        Test the send method of KafkaWrapper.
        Ensures that the message is published to the Kafka topic.
        """
        test_topic = 'test_topic'
        test_message = 'test_message'
        await self.wrapper.send(test_topic, test_message)
        
        self.wrapper.producer.send_and_wait.assert_called_once_with(test_topic, test_message)

    @patch('src.queue.kafka_wrapper.AIOKafkaConsumer', return_value=AsyncMock())
    async def test_receive(self, MockKafkaConsumer):
        """
        Test the receive method of KafkaWrapper.
        Ensures that the messages are correctly received from the Kafka topic.
        """
        test_topic = 'test_topic'
        test_message = 'test_message'
        async for message in self.wrapper.receive(test_topic):
            self.assertEqual(message, test_message)

    async def test_close(self):
        """
        Test the close method of KafkaWrapper.
        Ensures that the Kafka producer is stopped.
        """
        await self.wrapper.close()
        self.wrapper.producer.stop.assert_called_once()

# Entry point for the unit tests.
if __name__ == '__main__':
    unittest.main()

