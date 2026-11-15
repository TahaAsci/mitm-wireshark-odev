# MITM (Ortadaki Adam) Saldırısı ve Wireshark Paket Analizi

**Grup Üyeleri:** Taha, Resul, Yusuf

Bu projede Python socket kütüphanesi kullanılarak istemci (gönderici), aradaki vekil (MITM) ve alıcı sunucu arasında temel bir ağ iletişimi kurulmuştur. 3 kişi arasında roller dönüşümlü olarak değiştirilmiş ve araya giren kişinin şifrelenmemiş ağ paketlerini nasıl okuyabildiği Wireshark ile incelenmiştir.

## Rol Dağılımı

| Tur | Gönderen | Aradaki Kişi (MITM) | Alıcı |
| :--- | :--- | :--- | :--- |
| **1. Tur** | Taha | Yusuf | Resul |
| **2. Tur** | Yusuf | Taha | Resul |
| **3. Tur** | Taha | Resul | Yusuf |

## Dosyalar

- `alici.py` — Hedef sunucu (Port: 6000)
- `mitm.py` — Araya girip paketi yakalayan ve hedefe ileten vekil (Port: 5000)
- `gonderici.py` — Paketi MITM üzerinden alıcıya gönderen istemci
- `test_3_tur.py` — 3 turu arka arkaya çalıştıran test betiği
- `screenshots/` — Wireshark ekran görüntüleri

## Nasıl Çalıştırılır?

Tek bir komutla 3 turun tamamını çalıştırmak için:

```bash
py test_3_tur.py
```

Ayrı ayrı çalıştırmak için sıra şöyledir:
1. `py alici.py`
2. `py mitm.py`
3. `py gonderici.py`

## Wireshark Analizi

Wireshark'ta `tcp.port == 5000` filtresi uygulanmış ve yakalanan TCP paketine sağ tıklanarak **Follow -> TCP Stream** seçilmiştir:

### 1. Tur (Taha -> Yusuf [MITM] -> Resul)
![Tur 1 Wireshark](screenshots/tur1_wireshark.png)

### 2. Tur (Yusuf -> Taha [MITM] -> Resul)
![Tur 2 Wireshark](screenshots/tur2_wireshark.png)

### 3. Tur (Taha -> Resul [MITM] -> Yusuf)
![Tur 3 Wireshark](screenshots/tur3_wireshark.png)

## Sonuç

Şifresiz TCP bağlantılarında araya giren üçüncü bir taraf ağ trafiğini dinleyerek tüm veriyi açık metin (plaintext) olarak görebilmektedir. Bu durumun önüne geçmek için iletim katmanında SSL/TLS (HTTPS vb.) protokolleri kullanılmalıdır.
