from flask import Blueprint, g, jsonify
import time

# Define a new blueprint for the consumer component of the application.
consumer_blueprint = Blueprint('consumer', __name__)

@consumer_blueprint.route('/receive/<topic>', methods=['GET'])
async def receive_message(topic):
    """
    Asynchronous route to receive messages from a specific topic.
    """
    # Retrieve the message queue instance from the application context (g).
    message_queue = g.message_queue
    
    # Record the current time to calculate the total time taken for receiving messages.
    start_time = time.time()
    
    # Asynchronously receive messages from the message queue. Each message is decoded from UTF-8.
    # This is a list comprehension within an asynchronous operation, ensuring all messages for the topic are received.
    messages = [message.decode('utf-8') async for message in message_queue.receive(topic)]
    
    # Record the time after the messages have been received.
    end_time = time.time()
    
    # Calculate the elapsed time for the receive operation.
    elapsed_time = end_time - start_time
    
    # Update the metrics for the receive operation, including the elapsed time and number of messages.
    await g.metrics.update_receive_metrics(elapsed_time, len(messages))
    
    # Return a JSON response containing the topic and the received messages.
    return jsonify({"topic": topic, "messages": messages})

