import socket

# Alıcı (Hedef Sunucu)
HOST = '127.0.0.1'
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"Alıcı dinlemede... (Port: {PORT})")

conn, addr = server.accept()
print(f"Bağlantı geldi: {addr}")

veri = conn.recv(1024).decode('utf-8')
print("\n[ALICI] Paket başarıyla ulaştı!")
print("Mesaj:", veri)

conn.close()
server.close()
