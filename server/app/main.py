from flask import Flask, render_template
from flask_socketio import SocketIO
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    socketio = SocketIO(app)

    @socketio.on('connect')
    def connect():
        print('Client connected')

    @socketio.on('event')
    def handle_my_custom_event(json):
        print('received data: ' + str(json))


    @app.route('/')
    def hello_world():
        return render_template('index.html')

    return app, socketio