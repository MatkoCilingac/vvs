import socket
from io import StringIO

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 120))
s.listen()
print("Server čaká na pripojenie na porte 120...")

while True:
    connection, address = s.accept()

    print(f"Pripojil sa klient s adresou: {address}")
    poslta: str = input("zadaj spravu na poslanie > ")
    connection.sendall(poslta.encode("UTF-8"))

    data: str = connection.recv(1024).decode("UTF-8").strip()
    print(f"Prijaté dáta od klienta: {data}")

    connection.close()

#s:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("ip adresa serveru", 120))

#s.sendall("hello world".encode("utf-8"))

#data: str = s.recv(1024).decode("utf-8").strip()

#print(f"data: {data}")
#s.close()