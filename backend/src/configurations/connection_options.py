from pydantic import BaseModel

class ConnectionOptions(BaseModel):
    mod_path: str
    host: str
    port: int
    username: str = None
    password: str = None
    extra: dict = {}
