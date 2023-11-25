#server
from collections import deque
from socket import *
from select import select

addres = ('', 8000)
sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(addres)
sock.listen(5)

tasks = deque()
recv_wait = { }
send_wait = { }
input = [sock]

def run():
    global tasks, recv_wait, send_wait
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            #ожидание в\в
            #this shit dosnt work correct idk what he want
            can_recv, can_send, [] = select(recv_wait, send_wait, input)
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))

        task = tasks.popleft()
        try:
            why, what = next(task)
            if why == 'recv':
                recv_wait[why] = task
            elif why =='send':
                send_wait[why] = task
            else:
                raise RuntimeError("ARG?")
        except StopIteration:
            print('task done')

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_handler(client):
    while True:
        yield 'recv', client
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        yield 'send', client
        client.send(resp)
    print('close')

def fib_server():
    while True:
        yield 'recv', sock
        client, addr = sock.accept()
        print('Connection', addr)
        tasks.append(fib(client))

tasks.append(fib_server())
run()