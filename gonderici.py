import socket
import sys

# Gönderici (İstemci)
# Paketi doğrudan alıcıya değil, aradaki MITM'e (5000) yollar.

MITM_IP = '127.0.0.1'
MITM_PORT = 5000

print("Hangi turu göndermek istiyorsunuz?")
print("1 - Tur 1: Taha -> (Yusuf MITM) -> Resul")
print("2 - Tur 2: Yusuf -> (Taha MITM) -> Resul")
print("3 - Tur 3: Taha -> (Resul MITM) -> Yusuf")

tur = input("Seçiminiz (1/2/3) [Varsayılan: 1]: ").strip() or "1"

if tur == "1":
    mesaj = "Tur-1 | Gonderen: Taha | Yakalayan (MITM): Yusuf | Alici: Resul | Mesaj: Selam Resul naber?"
elif tur == "2":
    mesaj = "Tur-2 | Gonderen: Yusuf | Yakalayan (MITM): Taha | Alici: Resul | Mesaj: Resul odev bitti mi?"
elif tur == "3":
    mesaj = "Tur-3 | Gonderen: Taha | Yakalayan (MITM): Resul | Alici: Yusuf | Mesaj: Yusuf slaytlari hazirladin mi?"
else:
    mesaj = f"Ozel Mesaj: {tur}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((MITM_IP, MITM_PORT))
s.send(mesaj.encode('utf-8'))
s.close()

print("\n[+] Paket MITM uzerinden gonderildi:")
print(mesaj)
