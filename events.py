from extensions import socket
from flask import request
from flask_socketio import emit

users = {}

@socket.on('connect')
def connect_user(): 
    print('Client Connected')

@socket.on('joined')
def user_joined(name):
    users[request.sid] = name
    print(f'user {name} joined!!')

@socket.on('message')
def send_message(sms):
    print(f'user Send sms: {sms}')
    userName = None
    if request.sid in users:
        userName = users[request.sid]
        socket.emit('chat', {"sms" : sms, "user": userName} )
    