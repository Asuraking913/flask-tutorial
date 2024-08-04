from app import create_app
from events import socket

flask_app = create_app()

if __name__ == "__main__":
    socket.run(flask_app, debug = True)
    # flask_app.run()