from flask import Flask
from backend_monitoring import backend_monitoring

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(backend_monitoring)

if __name__ == '__main__':
    app.run(debug=True)
