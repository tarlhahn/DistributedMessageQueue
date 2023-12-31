# Distributed Message Queue System

A simple yet robust distributed message queue system that facilitates communication between multiple producers and consumers. This system ensures that messages are delivered at least once and provides a dashboard for monitoring various metrics.

__Trigger Alert:__ This is for demonstration purposes only. This is not intended for use in production.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features

- **Producers**: Send messages to the queue.
- **Consumers**: Retrieve messages from the queue.
- **Message Delivery Assurance**: Ensures that each message is delivered at least once.
- **Monitoring Dashboard**: Provides real-time insights into the number of messages in the queue, active producers, and consumers.

## Technologies Used

- **Backend**: Python
- **Messaging**: Kafka, extensible to other queues
- **Frontend**: Vue.js for the monitoring dashboard

## Getting Started

### Prerequisites
- Ensure you have Python installed. Recommend using virtual environments
  - required packages: aiokafka pytest-asyncio aio_pika Flask\[async\] pydantic flask-cors gunicorn uvicorn[standard]
- Install Node.js and npm/yarn for the dashboard.
- Set up Kafka or RabbitMQ as your message queue.

### Installation

**Clone the Repository**
```bash
git clone https://github.com/your-username/distributed-message-queue-system.git
cd distributed-message-queue-system
```
**Set Up the Backend**

#### Backend API
We recommend using a virtual environment for the backend api.
```bash
# From backend directory, before installing the necessary packages.
python -m venv myenv && source myenv/bin/activate
```

Install following packages
```bash
pip install aiokafka pytest-asyncio aio_pika Flask[async] pydantic flask-cors gunicorn uvicorn[standard]
```

```bash
cd DistributedMessageQueueSystem/backend/src
pip install .
```
### Message Queue
Follow the official documentation for [Kafka](https://kafka.apache.org/quickstart) to set up the messaging system.

#### Dashboard
```bash
cd DistributedMessageQueueSystem/dashboard
npm install # or yarn install
```
## Running the Application

### Backend
```bash
cd DistributedMessageQueueSystem/backend
gunicorn -w 1 -b 0.0.0.0:8000 src.backend:app
```
### Message Queue
Follow the official documentation for [Kafka](https://kafka.apache.org/quickstart) to start the messaging system.

### Dashboard
```bash
cd DistributedMessageQueueSystem/src/dashboard
npm start # or yarn start
```
## Usage

**Sending Messages (Producers)**
```bash
curl -X POST http://localhost:8080/send -d "message=Hello World"
```
**Receiving Messages (Consumers)**
```bash
curl http://localhost:8080/receive
```
**Access the Dashboard**
- Open a web browser and navigate to `http://localhost:3000`

## Running Tests

- **Backend & API**
```bash
cd DistributedMessageQueueSystem/backend/tests/unit/api
python -m pytest tests/
```

## Logging
Check the logs/ directory for system logs and potential issues.

## License

Distributed under the MIT License. See LICENSE for more information.

## Contact

Project Link: [https://github.com/tarlhahn/DistributedMessageQueue](https://github.com/tarlhahn/DistributedMessageQueue)
