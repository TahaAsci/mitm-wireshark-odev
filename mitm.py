import socket

# Ortadaki Adam (MITM Proxy)
# Gönderici 5000 portuna yollar, biz paketi okuruz ve alıcının 6000 portuna iletiriz.

MITM_PORT = 5000
ALICI_IP = '127.0.0.1'
ALICI_PORT = 6000

# 1. Göndericiden gelen paketi yakala
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', MITM_PORT))
server.listen(1)

print(f"MITM devrede, port {MITM_PORT} dinleniyor...")
conn, addr = server.accept()

paket = conn.recv(1024)
print("\n[!] MITM: Araya girildi, paket yakalandı!")
print("Paket içeriği:", paket.decode('utf-8'))

# 2. Yakalanan paketi alıcıya ilet
hedef = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hedef.connect((ALICI_IP, ALICI_PORT))
hedef.send(paket)
print("[+] Paket alıcıya aktarıldı.")

hedef.close()
conn.close()
server.close()
