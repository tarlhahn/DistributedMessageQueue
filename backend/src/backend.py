#backend.py
from asgiref.wsgi import WsgiToAsgi
from src.api.api import start

app = start()
asgi_app = WsgiToAsgi(app)
