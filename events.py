from extensions import socket
from flask import request
from flask_socketio import emit

users = {}

@socket.on('connect')
def handle_connect():
    print('Client connected')

@socket.on('user_join')
def handle_join(user): 
    print(f'User {user} joined')
    users[user] = request.sid
    print(users, "event")

@socket.on('message')
def handle_message(sms):
    print(f'user sent messag  {sms}')
    print(request.sid)
    userName = None
    for user in users:
        if users[user] == request.sid:
            userName = user
            emit('chat', {'sms' : f"{userName} : {sms}"}, broadcast=True)