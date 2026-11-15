import socket
import threading
import time

# Tek komutla 3 turu birden test etmek ve Wireshark yakalaması yapmak için yardımcı betik.

turlar = [
    "Tur-1 | Gonderen: Taha | Yakalayan (MITM): Yusuf | Alici: Resul | Mesaj: Selam Resul naber?",
    "Tur-2 | Gonderen: Yusuf | Yakalayan (MITM): Taha | Alici: Resul | Mesaj: Resul odev bitti mi?",
    "Tur-3 | Gonderen: Taha | Yakalayan (MITM): Resul | Alici: Yusuf | Mesaj: Yusuf slaytlari hazirladin mi?"
]

def tur_calistir(mesaj):
    alici = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alici.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    alici.bind(('127.0.0.1', 6000))
    alici.listen(1)

    mitm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mitm.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mitm.bind(('127.0.0.1', 5000))
    mitm.listen(1)

    def alici_thread():
        c, _ = alici.accept()
        gelen = c.recv(1024).decode('utf-8')
        print("  [Alıcıya Ulaştı]:", gelen)
        c.close()
        alici.close()

    def mitm_thread():
        c, _ = mitm.accept()
        veri = c.recv(1024)
        print("  [MITM Yakaladı]:", veri.decode('utf-8'))
        c.close()
        mitm.close()
        
        # Alıcıya aktar
        hedef = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hedef.connect(('127.0.0.1', 6000))
        hedef.send(veri)
        hedef.close()

    t_alici = threading.Thread(target=alici_thread)
    t_mitm = threading.Thread(target=mitm_thread)
    t_alici.start()
    t_mitm.start()
    time.sleep(0.2)

    # Gönderici
    g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g.connect(('127.0.0.1', 5000))
    g.send(mesaj.encode('utf-8'))
    g.close()

    t_alici.join()
    t_mitm.join()

print("=" * 50)
print("3 Turlu MITM Testi Başlıyor...")
print("=" * 50)

for i, m in enumerate(turlar, 1):
    print(f"\n>> Tur {i}:")
    tur_calistir(m)
    time.sleep(0.5)

print("\n" + "=" * 50)
print("Tamamlandı! Wireshark'ta paketleri kontrol edebilirsiniz.")
print("=" * 50)
