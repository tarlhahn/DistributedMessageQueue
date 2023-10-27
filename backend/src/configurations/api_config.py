from pydantic import BaseModel
from src.configurations.connection_options import ConnectionOptions

class AppConfig(BaseModel):
    mq_options: ConnectionOptions

