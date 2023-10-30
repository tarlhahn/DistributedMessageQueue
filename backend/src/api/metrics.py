import asyncio

class Metrics:
    def __init__(self):
        # Initialize metrics counters and accumulators
        self.total_messages_sent = 0
        self.total_messages_received = 0
        self.total_send_time = 0.0
        self.total_receive_time = 0.0
        self.last_send_throughput = 0.0
        self.last_receive_throughput = 0.0

        # Locks to ensure thread-safe updating of metrics
        self._send_lock = asyncio.Lock()
        self._receive_lock = asyncio.Lock()

    async def update_send_metrics(self, send_time):
        """
        Asynchronously update sending metrics after a message is sent.
        """
        async with self._send_lock:  # Ensure thread safety with async lock
            self.total_messages_sent += 1
            self.total_send_time += send_time
            # Calculate the last send throughput, avoid division by zero
            self.last_send_throughput = 1.0 / send_time if send_time > 0 else 0

    async def update_receive_metrics(self, receive_time, num_messages):
        """
        Asynchronously update receiving metrics after messages are received.
        """
        async with self._receive_lock:  # Ensure thread safety with async lock
            self.total_messages_received += num_messages
            self.total_receive_time += receive_time
            # Calculate the last receive throughput, avoid division by zero
            self.last_receive_throughput = num_messages / receive_time if receive_time > 0 and num_messages > 0 else 0

    @property
    async def average_lifetime_send_throughput(self):
        """
        Asynchronously calculate and return the average lifetime send throughput.
        """
        async with self._send_lock:  # Ensure thread safety with async lock
            # Avoid division by zero
            return self.total_messages_sent / self.total_send_time if self.total_send_time > 0 else 0

    @property
    async def average_lifetime_receive_throughput(self):
        """
        Asynchronously calculate and return the average lifetime receive throughput.
        """
        async with self._receive_lock:  # Ensure thread safety with async lock
            # Avoid division by zero
            return self.total_messages_received / self.total_receive_time if self.total_receive_time > 0 else 0
    
    async def to_dict(self):
        """
        Asynchronously gather all the metrics and return them as a dictionary.
        """
        return {
            "total_messages_sent": self.total_messages_sent,
            "total_messages_received": self.total_messages_received,
            "total_send_time": self.total_send_time,
            "total_receive_time": self.total_receive_time,
            "last_send_throughput": self.last_send_throughput,
            "last_receive_throughput": self.last_receive_throughput,
            "average_lifetime_send_throughput": await self.average_lifetime_send_throughput,
            "average_lifetime_receive_throughput": await self.average_lifetime_receive_throughput,
        }

