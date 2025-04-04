"""import datetime

# Uçuş bilgilerini saklayan sözlük
ucuslar = {}
rotalar = [
    ("İstanbul", "Ankara"), ("Ankara", "İstanbul"),
    ("İstanbul", "İzmir"), ("İzmir", "İstanbul"),
    ("İstanbul", "Antalya"), ("Antalya", "İstanbul")
]
baslangic_saati = datetime.datetime.strptime("06:00", "%H:%M")
bitis_saati = datetime.datetime.strptime("23:30", "%H:%M")
aralik = datetime.timedelta(minutes=30)

# Uçuş saatlerini oluşturma
temp_time = baslangic_saati
while temp_time <= bitis_saati:
    for rota in rotalar:
        ucuslar[(rota[0], rota[1], temp_time.strftime("%H:%M"))] = []
    temp_time += aralik

# Kullanıcı bilgileri
ad = "Ahmet"
soyad = "Yılmaz"
tc = "12345678901"
kalkis = "İstanbul"
varis = "Ankara"
saat = "08:30"
bilet_turu = "ekonomi"
gidis_donus = True
otel = False
yolcu_turu = "çocuk"

# TC kimlik numarası doğrulama
if not (tc.isdigit() and len(tc) == 11):
    print("Hatalı TC Kimlik Numarası!")
else:
    ucus_anahtari = (kalkis, varis, saat)
    if ucus_anahtari not in ucuslar:
        print("Uçuş bulunamadı!")
    elif len(ucuslar[ucus_anahtari]) >= 12:
        print("Uçak dolu!")
    else:
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

        # Çocuk için indirim
        if yolcu_turu == "çocuk":
            fiyat -= 3000
            if fiyat < 0:
                fiyat = 0

        # Gidiş dönüş indirimi
        if gidis_donus:
            fiyat = fiyat * 2 * 0.9

        # Otel ek ücreti
        if otel:
            fiyat += 4000

        ucuslar[ucus_anahtari].append(tc)
        print(f"Rezervasyon başarılı! Toplam ücret: {fiyat} TL")
"""
import datetime

# Uçuş bilgilerini saklayan sözlük
ucuslar = {}
rotalar = [
    ("İstanbul", "Ankara"), ("Ankara", "İstanbul"),
    ("İstanbul", "İzmir"), ("İzmir", "İstanbul"),
    ("İstanbul", "Antalya"), ("Antalya", "İstanbul")
]
baslangic_saati = datetime.datetime.strptime("06:00", "%H:%M")
bitis_saati = datetime.datetime.strptime("23:30", "%H:%M")
aralik = datetime.timedelta(minutes=30)

# Uçuş saatlerini oluşturma
temp_time = baslangic_saati
while temp_time <= bitis_saati:
    for rota in rotalar:
        ucuslar[(rota[0].lower(), rota[1].lower(), temp_time.strftime("%H:%M"))] = {"yolcular": [], "koltuklar": list(
            range(1, 13))}  # Tüm uçuşları boş kabul et
    temp_time += aralik

# Kullanıcı bilgilerini al
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
tc = input("TC Kimlik Numaranızı girin (11 haneli): ")
kalkis = input("Kalkış şehrini girin: ").strip().lower()  # Küçük harfe çevir
varis = input("Varış şehrini girin: ").strip().lower()  # Küçük harfe çevir
saat = input("Uçuş saatini girin (Örn: 08:30): ").strip()

# Uçuş saatinin geçerli olup olmadığını kontrol et
ucus_saatleri = [temp_time.strftime("%H:%M") for temp_time in
                [baslangic_saati + aralik * i for i in range(int((bitis_saati - baslangic_saati) // aralik))]]
if saat not in ucus_saatleri:
    print("Geçersiz uçuş saati. Lütfen geçerli bir saat dilimi seçin.")
else:
    bilet_turu = input("Bilet türünü seçin (ekonomi/business): ").strip().lower()  # Küçük harfe çevir
    gidis_donus = input("Gidiş-Dönüş mü? (E/H): ").strip().lower() == "e"  # Küçük harfe çevir
    otel = input("Otel eklemek ister misiniz? (E/H): ").strip().lower() == "e"  # Küçük harfe çevir
    yolcu_turu = input("Yolcu türünü seçin (yetişkin/çocuk): ").strip().lower()  # Küçük harfe çevir

    # TC kimlik numarası doğrulama
    if not (tc.isdigit() and len(tc) == 11):
        print("Hatalı TC Kimlik Numarası!")
    else:
        # Uçuş anahtarını kontrol et
        ucus_anahtari = (kalkis, varis, saat)
        if ucus_anahtari not in ucuslar:
            print("Uçuş bulunamadı!")
        else:
            # Uçuş bulundu ve boş yer kontrolü
            mevcut_yerler = 12 - len(ucuslar[ucus_anahtari]["yolcular"])  # Mevcut boş yer sayısı
            if mevcut_yerler <= 0:
                print("Uçak dolu!")
            else:
                print(f"Uçuş bulundu! {mevcut_yerler} kişilik yer mevcut.")

                # Koltuk seçimi
                while True:
                    # Mevcut boş koltukları listele (önceki seçilen koltukları gizle)
                    bos_koltuklar = [str(koltuk) for koltuk in ucuslar[ucus_anahtari]["koltuklar"] if
                                    koltuk not in ucuslar[ucus_anahtari]["yolcular"]]
                    if not bos_koltuklar:
                        print("Tüm koltuklar dolmuş!")
                        break

                    koltuk_numarasi = int(
                        input(f"Bir koltuk numarası seçin (Boş koltuklar: {', '.join(bos_koltuklar)}): "))

                    # Koltuk numarasının geçerli olup olmadığını ve dolu olup olmadığını kontrol et
                    if koltuk_numarasi not in ucuslar[ucus_anahtari]["koltuklar"]:
                        print("Geçersiz koltuk numarası!")
                    elif koltuk_numarasi in ucuslar[ucus_anahtari]["yolcular"]:
                        print("Bu koltuk zaten dolu! Lütfen başka bir koltuk seçin.")
                    else:
                        # Koltuk seçimini kaydet ve koltukları güncelle
                        ucuslar[ucus_anahtari]["yolcular"].append(koltuk_numarasi)

                        # Koltuğu boş koltuklar listesinden çıkar, dolu koltuklar listesine ekle
                        bos_koltuklar.remove(str(koltuk_numarasi))

                        # Koltuk sayısını güncelle
                        dolu_koltuk_sayisi = len(ucuslar[ucus_anahtari]["yolcular"])
                        bos_koltuk_sayisi = 12 - dolu_koltuk_sayisi

                        print(f"Koltuk numarası {koltuk_numarasi} başarıyla rezerve edildi!")
                        print(f"Boş Koltuklar: {bos_koltuk_sayisi}")
                        print(f"Dolu Koltuklar: {dolu_koltuk_sayisi}")
                        break  # Koltuk seçimi tamamlandı, döngüyü kır

                    # Koltuk seçiminde hata durumu: tekrar sorulacak

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

                    # Çocuk için indirim
                    if yolcu_turu == "çocuk":
                        fiyat -= 3000
                        if fiyat < 0:
                            fiyat = 0

                    # Gidiş dönüş indirimi
                    if gidis_donus:
                        fiyat = fiyat * 2 * 0.9

                    # Otel ek ücreti
                    if otel:
                        fiyat += 4000

                    # Rezervasyonu kaydet ve tüm yolcu bilgilerini göster
                    print(f"\nRezervasyon başarılı!")
                    print(f"\nYolcu Bilgileri:")
                    print(f"Ad: {ad}")
                    print(f"Soyad: {soyad}")
                    print(f"TC: {tc}")
                    print(f"Kalkış: {kalkis.capitalize()}")
                    print(f"Varış: {varis.capitalize()}")
                    print(f"Saat: {saat}")
                    print(f"Bilet Türü: {bilet_turu.capitalize()}")
                    print(f"Yolcu Türü: {yolcu_turu.capitalize()}")
                    print(f"Otel: {otel}")
                    print(f"Gidiş-Dönüş: {gidis_donus}")
                    print(f"Seçilen Koltuk: {koltuk_numarasi}")
                    print(f"Toplam ücret: {fiyat} TL")











