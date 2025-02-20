from flask import Flask

from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandle

from src.main.routes.products_routes import products_routes_bp

redis_connection_handle = RedisConnectionHandler()
sqlite_connection_handle = SqliteConnectionHandle()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

app = Flask(__name__)


app.register_blueprint(products_routes_bp)
