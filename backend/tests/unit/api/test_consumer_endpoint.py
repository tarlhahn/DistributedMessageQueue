import unittest
from flask import Flask, jsonify
from src.api.api import create_app
from src.api.consumer_endpoint import consumer_blueprint
from unittest.mock import Mock, AsyncMock, patch

from src.configurations.api_config import AppConfig
from src.configurations.connection_options import ConnectionOptions

class TestConsumerEndpoint(unittest.IsolatedAsyncioTestCase):

    async def async_generator(self, messages):
        # Asynchronous generator to simulate receiving messages
        for message in messages:
            yield message

    def setUp(self):
        """
        Setup for 'receive_message' test
        """
        # Initialize configurations for the test case
        # Here, we're not mocking the options but using real instances with test values
        options = AppConfig(
            mq_options=ConnectionOptions(
                mod_path='src.queue.kafka_wrapper.KafkaWrapper',
                host='localhost',
                port=5672,
            )
        )
        
        # Create a mock for the message queue and simulate its behavior
        message_queue = Mock()
        # Mock the 'receive' method to return a generator that yields a sample message
        message_queue.receive.return_value = self.async_generator(["Sample message from queue".encode('utf-8')])

        # Create the application instance using the configurations and mocked message queue
        app = create_app(options, message_queue)
        # Get the test client for the Flask application
        self.client = app.test_client()

    @patch('src.api.consumer_endpoint.receive_message', new_callable=AsyncMock)  # Mock the actual receiving logic
    def test_receive_message(self, mock_receive):
        """
        Test case to verify the functionality of the 'receive_message' endpoint.
        This function simulates a GET request and checks the response.
        """
        # Simulate a GET request to the 'receive' endpoint and store the response
        response = self.client.get('/receive/a_topic')
        # Assert that the HTTP response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Parse the response data as JSON
        json_data = response.get_json()
        # Assert that the received messages match the expected sample message
        self.assertEqual(json_data["messages"], ["Sample message from queue"])

if __name__ == '__main__':
    # If this script is run as the main program, execute the tests
    unittest.main()

