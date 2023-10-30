import unittest
from unittest.mock import AsyncMock, patch

from flask import Flask
from src.api.api import create_app
from src.api.monitoring_endpoint import monitoring_blueprint

from src.configurations.api_config import AppConfig
from src.configurations.connection_options import ConnectionOptions

# Define a test class for the Monitoring Endpoint
class TestMonitoringEndpoint(unittest.TestCase):

    # This method is called before each test in the test class
    def setUp(self):
        """
        Setup for 'monitoring' test
        """
        # Define configuration options for the application
        # (e.g., message queue connection details)
        options = AppConfig(
            mq_options=ConnectionOptions(
                mod_path='src.queue.kafka_wrapper.KafkaWrapper',
                host='localhost',
                port=5672,
                username='user',
                password='pass'
            )
        )
        
        # Create a mock for the message queue to simulate its behavior without actual interactions
        message_queue = AsyncMock()

        # Create an instance of the Flask app with the given options and mock message queue
        app = create_app(options, message_queue)
        # Create a test client for the Flask app to simulate HTTP requests
        self.client = app.test_client()

    # Define a test case for the monitoring endpoint
    def test_monitoring(self):
        """
        Test case to verify the functionality of the 'monitoring' endpoint.
        This function simulates a GET request and checks the response.
        """
        # Send a GET request to the monitoring endpoint
        response = self.client.get('/monitoring')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Parse the JSON data from the response
        json_data = response.get_json()
        # Uncomment the following lines if you want to assert specific values in the response
        #self.assertEqual(json_data["active_producers"], 5)
        #self.assertEqual(json_data["active_consumers"], 3)
        #self.assertEqual(json_data["messages_in_queue"], 100)

# If this script is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()

