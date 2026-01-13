# 💬 Real-Time Chat Application (Python & Flask-SocketIO)

A lightweight, bidirectional communication chat server built with Python and Flask. This application uses WebSockets to allow multiple users to chat instantly without refreshing their browsers.


## 🚀 Features
* **Real-Time Messaging**: Messages are delivered instantly to all connected clients.
* **Bi-directional Communication**: Uses Socket.io to allow both the server and client to send data at any time.
* **Broadcasting**: Messages received by the server are echoed to every active user.
* **Cross-Origin Support**: Configured to allow connections from different browser tabs and origins.

## 🛠️ Tech Stack
* **Backend**: Python, Flask
* **Real-Time Engine**: Flask-SocketIO (WebSockets)
* **Frontend**: HTML5, CSS3, Socket.io Client JS

## 📦 Installation & Setup

### 1. Install Dependencies
You will need the Flask-SocketIO package. Install it via pip:

```bash
pip install flask flask-socketio
2. File Structure
Ensure your project is organized as follows:

Plaintext

├── app.py              # The Flask-SocketIO server
└── templates/
    └── index.html      # The chat interface
3. Run the Server
Execute the Python script:

Bash

python app.py
The server will start on http://127.0.0.1:5000. Open this URL in multiple browser tabs to test the real-time interaction.

💡 How It Works
Connection: When a user opens the page, a WebSocket handshake is performed between the browser and the Flask server.

Sending: When a user clicks 'Send', the client emits a message event to the server.

Handling: The @socketio.on('message') decorator in app.py catches the data.

Broadcasting: The server uses emit('message', data, broadcast=True) to push that data out to every other connected socket.

🛠️ Future Enhancements
[ ] Usernames: Allow users to set a custom nickname.

[ ] Persistent Storage: Save chat logs to a SQLite database.

[ ] Typing Indicators: Show "User is typing..." notifications.

[ ] Private Rooms: Enable private one-on-one chatting.
