from flask import Flask
from flask_cors import CORS
from config import Config

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    from name.routes import name
    app.register_blueprint(name)
    return app      

    