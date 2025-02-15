from flask import Flask, render_template
from .socket_handlers import socketio
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    socketio.init_app(app)

    # This will be moved in the future
    @app.route('/')
    def hello_world():
        return render_template('index.html')

    return app, socketio