import datetime
import json
import os

# Kullanıcılar
kullanicilar = {
    "ali": "1234",
    "ayse": "5678",
    "veli": "4321",
    "fatma": "8765",
    "admin": "admin"
}

# JSON'a rezervasyon kaydetme fonksiyonu
def rezervasyon_kaydet(rezervasyon):
    dosya_adi = "rezervasyonlar.json"
    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            try:
                veriler = json.load(dosya)
            except json.JSONDecodeError:
                veriler = []
    else:
        veriler = []

    veriler.append(rezervasyon)

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, indent=4, ensure_ascii=False)

# Giriş sistemi
print("=== GİRİŞ EKRANI ===")
k_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")

if k_adi not in kullanicilar or kullanicilar[k_adi] != sifre:
    print("Hatalı kullanıcı adı veya şifre!")
    exit()
else:
    print(f"Hoş geldiniz, {k_adi}!\n")

# Uçuş bilgileri
ucuslar = {}
rotalar = [
    ("İstanbul", "Ankara"), ("Ankara", "İstanbul"),
    ("İstanbul", "İzmir"), ("İzmir", "İstanbul"),
    ("İstanbul", "Antalya"), ("Antalya", "İstanbul")
]
baslangic_saati = datetime.datetime.strptime("06:00", "%H:%M")
bitis_saati = datetime.datetime.strptime("23:30", "%H:%M")
aralik = datetime.timedelta(minutes=30)

temp_time = baslangic_saati
while temp_time <= bitis_saati:
    for rota in rotalar:
        ucuslar[(rota[0].lower(), rota[1].lower(), temp_time.strftime("%H:%M"))] = {
            "yolcular": [],
            "koltuklar": list(range(1, 13))
        }
    temp_time += aralik

# Kullanıcıdan bilgiler alınır
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
tc = input("TC Kimlik Numaranız (11 haneli): ")
if not (tc.isdigit() and len(tc) == 11):
    print("Hatalı TC!")
    exit()

kalkis = input("Kalkış şehri: ").strip().lower()
varis = input("Varış şehri: ").strip().lower()
saat = input("Uçuş saati (Örn: 08:30): ").strip()

gecerli_saatler = [(baslangic_saati + aralik * i).strftime("%H:%M") for i in range(
    int((bitis_saati - baslangic_saati) // aralik) + 1)]

if saat not in gecerli_saatler:
    print("Geçersiz saat seçimi.")
    exit()

ucus_anahtari = (kalkis, varis, saat)
if ucus_anahtari not in ucuslar:
    print("Uçuş bulunamadı.")
    exit()

mevcut_yerler = 12 - len(ucuslar[ucus_anahtari]["yolcular"])
if mevcut_yerler <= 0:
    print("Uçak dolu.")
    exit()
else:
    print(f"{mevcut_yerler} koltuk mevcut.")

# Koltuk seçimi
bos_koltuklar = [str(k) for k in ucuslar[ucus_anahtari]["koltuklar"] if k not in ucuslar[ucus_anahtari]["yolcular"]]
while True:
    print(f"Boş Koltuklar: {', '.join(bos_koltuklar)}")
    try:
        koltuk = int(input("Koltuk numarası seçin: "))
    except ValueError:
        print("Sayı girin.")
        continue

    if str(koltuk) not in bos_koltuklar:
        print("Geçersiz veya dolu koltuk.")
    else:
        ucuslar[ucus_anahtari]["yolcular"].append(koltuk)
        break

# Diğer bilgiler
bilet_turu = input("Bilet türü (ekonomi/business): ").strip().lower()
gidis_donus = input("Gidiş-Dönüş mü? (E/H): ").strip().lower() == "e"
otel = input("Otel eklemek ister misiniz? (E/H): ").strip().lower() == "e"
yolcu_turu = input("Yolcu türü (yetişkin/çocuk): ").strip().lower()

# Fiyat hesaplama
temel_fiyatlar = {
    "sabah": {"ekonomi": 4600, "business": 8900},
    "ogle": {"ekonomi": 5500, "business": 9800},
    "aksam": {"ekonomi": 6300, "business": 11000}
}
saat_dilim = int(saat.split(":")[0])
if 6 <= saat_dilim < 12:
    fiyat = temel_fiyatlar["sabah"][bilet_turu]
elif 12 <= saat_dilim < 18:
    fiyat = temel_fiyatlar["ogle"][bilet_turu]
else:
    fiyat = temel_fiyatlar["aksam"][bilet_turu]

if yolcu_turu == "çocuk":
    fiyat -= 3000
    fiyat = max(fiyat, 0)

if gidis_donus:
    fiyat = fiyat * 2 * 0.9

if otel:
    fiyat += 4000

# Bilgileri yazdır
print("\n=== Rezervasyon Başarılı ===")
print(f"Ad: {ad}")
print(f"Soyad: {soyad}")
print(f"TC: {tc}")
print(f"Kalkış: {kalkis.capitalize()}")
print(f"Varış: {varis.capitalize()}")
print(f"Saat: {saat}")
print(f"Bilet Türü: {bilet_turu.capitalize()}")
print(f"Yolcu Türü: {yolcu_turu.capitalize()}")
print(f"Gidiş-Dönüş: {'Evet' if gidis_donus else 'Hayır'}")
print(f"Otel: {'Evet' if otel else 'Hayır'}")
print(f"Koltuk No: {koltuk}")
print(f"Toplam Ücret: {fiyat} TL")

# JSON'a kaydet
rezervasyon_kaydet({
    "ad": ad,
    "soyad": soyad,
    "tc": tc,
    "kalkis": kalkis,
    "varis": varis,
    "saat": saat,
    "bilet_turu": bilet_turu,
    "yolcu_turu": yolcu_turu,
    "gidis_donus": gidis_donus,
    "otel": otel,
    "koltuk": koltuk,
    "ucret": fiyat
})
