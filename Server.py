import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)
print(conn)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(pickle.loads(data))

conn.close()

