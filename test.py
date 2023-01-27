import socket
import pickle
import threading
import time

from client import socketClient

def recibir():
    while True:
        data = s.receive()
        if not data:
            continue
        print(data)

def printPost(data, socket_):
    print('-> ', data['post'])

s = socketClient('localhost', 8080)
s.connect()

r = threading.Thread(target=recibir, daemon=True)
r.start()

s.addFunction('post', printPost)

room = input('room: ')
if len(room) > 0:
    s.join(room)
time.sleep(.5)

to = input('usuario: ')

while True:
    post = input('mensaje: ')
    if post == '0':
        break
    if len(room) > 0:
        s.roomDo(room, 'post', {'post': post})
    elif len(to) > 0:
        s.userDo(to, 'post', {'post': post})
    time.sleep(0.2)

s.roomDo('', 'leaveAll', {})
time.sleep(.5)

s.socket_.close()