# Fatura ödeme uygulaması

# Kullanıcı bilgileri
kullanicilar = {
    "ali": "1234",
    "ayse": "5678"
}

# KDV oranı
KDV = 1.2


# Login fonksiyonu
def login():
    print("Fatura Ödeme Sistemi - Giriş Yap")
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")

    if kullanicilar.get(kullanici_adi) == sifre:
        print(f"Hoş geldiniz, {kullanici_adi}!")
        return True
    else:
        print("Hatalı kullanıcı adı veya şifre!")
        return False


# Elektrik faturası hesaplama
def elektrik_faturasi_hesapla(kwh):
    birim_fiyat = 2.07
    return KDV * birim_fiyat * kwh


# Su faturası hesaplama
def su_faturasi_hesapla(m3, kategori):
    fiyat = 0
    if kategori.lower() == "mesken":
        if m3 <= 30:
            fiyat = 16.16
        elif m3 <= 60:
            fiyat = 21.54
        else:
            fiyat = 30.04
    elif kategori.lower() in ["resmi", "hastane"]:
        fiyat = 24.24
    elif kategori.lower() == "isyeri":
        if m3 <= 120:
            fiyat = 20.92
        else:
            fiyat = 30.04
    else:
        print("Geçersiz su faturası kategorisi.")
        return 0
    return KDV * fiyat * m3


# Doğal gaz faturası hesaplama
def dogalgaz_faturasi_hesapla(m3):
    birim_fiyat = 8.257027
    return KDV * birim_fiyat * m3


# Genel fatura ödeme fonksiyonu
def fatura_odeme():
    print("\nFatura Türleri: elektrik, su, dogalgaz")
    fatura_tipi = input("Lütfen fatura türünü girin: ").lower()

    if fatura_tipi == "elektrik":
        kwh = float(input("Tüketilen kWh miktarı: "))
        toplam = elektrik_faturasi_hesapla(kwh)
        print(f"Elektrik faturası tutarı: {toplam:.2f} TL")

    elif fatura_tipi == "su":
        m3 = float(input("Tüketilen su (m3): "))
        kategori = input("Kullanım türü (mesken, isyeri, resmi, hastane): ")
        toplam = su_faturasi_hesapla(m3, kategori)
        print(f"Su faturası tutarı: {toplam:.2f} TL")

    elif fatura_tipi == "dogalgaz":
        m3 = float(input("Tüketilen doğalgaz (m3): "))
        toplam = dogalgaz_faturasi_hesapla(m3)
        print(f"Doğal gaz faturası tutarı: {toplam:.2f} TL")

    else:
        print("Geçersiz fatura türü.")


# Ana program
if login():
    while True:
        fatura_odeme()
        devam = input("Başka bir fatura ödemek ister misiniz? (e/h): ")
        if devam.lower() != "e":
            print("Çıkış yapılıyor. İyi günler!")
            break
