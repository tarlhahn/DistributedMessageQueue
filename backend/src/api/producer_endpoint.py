# Import necessary modules and objects
from flask import Blueprint, g, request, jsonify
import time

# Create a new blueprint for the producer endpoints
producer_blueprint = Blueprint('producer', __name__)

@producer_blueprint.route('/send/<topic>', methods=['POST'])
async def send_message(topic):
    """
    Asynchronous route to send a message to a specific topic.
    """
    # Retrieve the JSON data from the request
    data = request.get_json()
    
    # Extract the message from the data
    message = data.get('message')

    # Record the current time to calculate the elapsed time later
    start_time = time.time()

    # Start the message queue, send the message, and then close the queue
    await g.message_queue.start()
    await g.message_queue.send(topic, message.encode('utf-8'))  # Encode the message to UTF-8
    await g.message_queue.close()

    # Record the time after the message is sent
    end_time = time.time()
    
    # Calculate the time taken to send the message
    elapsed_time = end_time - start_time

    # Update the metrics for the send operation with the elapsed time
    
    # Return a JSON response with the status and message details
    return jsonify({"status": "Message sent", "topic": topic, "message": message})

