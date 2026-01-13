from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# cors_allowed_origins="*" allows any browser tab to connect
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# This triggers when someone sends a message
@socketio.on('message')
def handle_message(data):
    print(f"Message received: {data}")
    # broadcast=True sends the message to EVERYONE connected
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)