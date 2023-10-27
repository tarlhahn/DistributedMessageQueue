# Importing necessary modules for testing
import unittest
from flask import Flask, jsonify  # for handling the server and JSON responses
from src.api.api import create_app  # function to create a Flask app instance
from src.api.producer_endpoint import producer_blueprint  # specific endpoint for message production
from unittest.mock import AsyncMock, patch  # for mocking asynchronous calls and patching

# Importing configurations
from src.configurations.api_config import AppConfig  # configuration settings for the API
from src.configurations.connection_options import ConnectionOptions  # connection settings for the message queue

# Defining a test case class for the producer endpoint, inheriting from asynchronous test case class
class TestProducerEndpoint(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        """
        Set up the test environment before each test case.
        This includes configurations, mocks, and the Flask test client.
        """

        # Define the configuration options for the message queue
        options = AppConfig(
            mq_options=ConnectionOptions(
                mod_path='src.queue.kafka_wrapper.KafkaWrapper',  # path to the message queue module
                host='localhost',  # the host of the message queue
                port=5672  # the port of the message queue
            )
        )
        
        # Create a mock for the message queue using AsyncMock for asynchronous calls
        message_queue = AsyncMock()

        # Create an instance of the Flask application with the given configurations and message queue
        app = create_app(options, message_queue)
        # Set up a test client for the Flask application for HTTP request simulation
        self.client = app.test_client()

    def test_send_message(self):
        """
        Test case to verify the functionality of the 'send_message' endpoint.
        This function simulates a POST request and checks the response.
        """

        # Simulate a POST request to the 'send_message' endpoint with JSON payload
        response = self.client.post('/send/a_topic', json={"message": "Hello World"})

        # Assert that the HTTP response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Parse the JSON data from the response
        json_data = response.get_json()
        # Assert that the "status" field in the JSON response is as expected
        self.assertEqual(json_data["status"], "Message sent")
        # Assert that the "message" field in the JSON response matches the sent message
        self.assertEqual(json_data["message"], "Hello World")

if __name__ == '__main__':
    unittest.main()

