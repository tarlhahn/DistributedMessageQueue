from abc import ABC, abstractmethod

class MessageQueueWrapperABC(ABC):
    """
    Abstract base class for message queue wrappers.

    This class defines the standard interface for all message queue wrappers.
    Concrete implementations should provide their own logic for sending, receiving, and closing connections.
    """
    
    def __init__(self, options):
        """
        Initialize the message queue wrapper with specified connection options.

        Args:
            options (ConnectionOptions): The connection options.
        """
        self.options = options
    
    @abstractmethod
    async def start(self):
        """
        Start the message queue interface.
        
        Raises:
            Exception: If there's an error starting the connection or producer.
        """
        pass
        
    @abstractmethod
    async def send(self, topic, message):
        """
        Send a message to the specified topic or queue.

        Args:
            topic (str): The topic or queue to send the message to.
            message (str): The message to send.

        Raises:
            Exception: If there's an error sending the message.
        """
        pass

    @abstractmethod
    async def receive(self, topic):
        """
        Asynchronously receive messages from the specified topic or queue.

        Args:
            topic (str): The topic or queue to receive messages from.

        Yields:
            str: Received messages.

        Raises:
            Exception: If there's an error receiving messages.
        """
        pass

    @abstractmethod
    async def close(self):
        """
        Close the connection or producer.

        Raises:
            Exception: If there's an error closing the connection or producer.
        """
        pass

