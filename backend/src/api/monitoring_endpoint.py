# Import necessary modules from Flask
from flask import Blueprint, g, jsonify

# Create a Blueprint for the monitoring endpoint
# This allows for organizing the application into distinct components
monitoring_blueprint = Blueprint('monitoring', __name__)

# Define a route for the monitoring endpoint
# This endpoint responds to GET requests at the '/monitoring' URL
@monitoring_blueprint.route('/monitoring', methods=['GET'])
async def monitoring():
    """
    Asynchronous route to fetch monitoring metrics.
    """
    # Fetch the monitoring data (e.g., metrics) from the global `g` object
    # The `g` object in Flask is used to store data that might be accessed by multiple functions during a request
    metrics_dict = await g.metrics.to_dict()
    
    # Convert the monitoring data to JSON format and return it as the response
    return jsonify(metrics_dict)

