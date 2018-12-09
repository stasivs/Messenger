import socket
import pickle


obj = ["Nickname", "Message"]
output = pickle.dumps(obj)
print(obj, output)

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(output)

sock.close()
