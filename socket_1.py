
# from socket import *
# def test_socket(addres=('', 8000)):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(addres)
#     sock.listen(5)


#     while True:
#         conn, addr = sock.accept()
#         print("connection", addr)
#         while True:
#             data = conn.recv(100)
#             if not data:
#                 break
#             req = int(data)
#             conn.send(req)
#             print("we have some trubles")


# if __name__ == "__main__":
#     test_socket()



from socket import *
 
server = socket(AF_INET, SOCK_STREAM)            # создаем объект сокета сервера
port = 8000                       # устанавливаем порт сервера
server.bind(("", port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
 
print("Server running")
while True:
    con, _ = server.accept()     # принимаем клиента
    data = con.recv(1024)           # получаем данные от клиента
    message = data.decode()         # преобразуем байты в строку
    print(f"Client sent: {message}")
    message = message[::-1]         # инвертируем строку
    con.send(message.encode())      # отправляем сообщение клиенту      