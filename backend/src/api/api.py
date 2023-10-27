# Import necessary modules and objects
from flask import Flask, g
from flask_cors import CORS
from src.configurations.api_config import AppConfig
from src.configurations.connection_options import ConnectionOptions
from src.api.producer_endpoint import producer_blueprint
from src.api.consumer_endpoint import consumer_blueprint
from src.api.monitoring_endpoint import monitoring_blueprint
from src.api.api_utils import create_message_queue
from src.api.metrics import Metrics
import asyncio

# Global variable for the message queue
mq = None

def create_app(options, message_queue):
    """
    Function to initialize the Flask application with necessary configurations, 
    global variables, and register the API blueprints.
    """
    app = Flask(__name__)  # Create a Flask app instance
    CORS(app)  # Enable Cross-Origin Resource Sharing for the app

    @app.before_request
    async def before_request():
        """
        Set up global variables before each request.
        """
        if 'message_queue' not in g:
            g.message_queue = message_queue  # Set the global message queue
        
    # Register the blueprints for different API endpoints
    app.register_blueprint(producer_blueprint)
    app.register_blueprint(consumer_blueprint)
    app.register_blueprint(monitoring_blueprint)

    return app  # Return the configured Flask app instance

def start():
    """
    Function to start the Flask application with specific configurations.
    """
    # Define configuration options for the message queue
    options = AppConfig(
        mq_options=ConnectionOptions(
            mod_path='src.queue.kafka_wrapper.KafkaWrapper',
            host='localhost',
            port=9092
        )
    )
    
    mq = create_message_queue(options.mq_options)  # Initialize the message queue
    app = create_app(options, mq)  # Create the Flask app with the given options
    return app  # Return the Flask app to be run
    
if __name__ == '__main__':
    # start 
    asyncio.run(start())

