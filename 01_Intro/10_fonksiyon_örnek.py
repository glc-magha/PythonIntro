"""def toplama():
    x = int(input('Lütfen bir sayı giriniz: '))
    y = int(input('Lütfen bir sayı giriniz: '))
    toplam = x + y

    print(toplam)
    print('{} + {} = {}'.format(x, y, toplam))
    print(f'{x} + {y} = {toplam}')
# toplama()



def kare_hesapla():
    kenar = int(input('Kenar: '))
    alan = kenar * kenar
    cevre = 4 * kenar

    print('Alan: ', alan)
    print(f'Cevre: {cevre}')
    print('Cevre: {}'.format(cevre))
# kare_hesapla()


def dikdortgen_hesapla():
    kisa_kenar = int(input('Kısa Kenarı: '))
    uzun_kenar = int(input('Uzun Kenarı: '))
    alan = kisa_kenar * uzun_kenar
    cevre = 2 * (kisa_kenar + uzun_kenar)

    print('Alan: ', alan)
    print(f'Cevre: {cevre}')
    print('Cevre: {}'.format(cevre))
# dikdortgen_hesapla()


def hesap_makinesi():
    print("Seçiminizi yapın:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminizi yapın (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == '2':
            print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif secim == '3':
            print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif secim == '4':
            if sayi2 == 0:
                print("Bir sayıyı sıfıra bölemezsiniz!")
            else:
                print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz giriş")
# hesap_makinesi()

def tek_cift_bul():
    number = int(input('Sayı: '))
    if number % 2 == 0:
        print(f'{number} çifttir...')
    else:
        print(f'{number} tektir...')

# tek_cift_bul()

def buyuk_sayiyi_bul():
    x = int(input('Sayı: '))
    y = int(input('Sayı: '))

    if x > y:
        print(f'{x} büyüktür...')
    elif x == y:
        print(f'{y}, {x} eşittir..')
    else:
        print(f'{y} büyüktür...')
# buyuk_sayiyi_bul()



def sayi_durumu(x):
    if x > 0:
        print(f'{x} pozitiftir')
    elif x < 0:
        print(f'{x} negatiftir')
    else:
        print(f'{x} nötrdür')
# Kullanıcıdan input alma
x = int(input('Sayı:  '))
sayi_durumu(x)



def mevsim_aylari(mevsim):
    mevsim = mevsim.lower()
    if mevsim == 'ilkbahar':
        return 'Mart, Nisan, Mayıs'
    elif mevsim == 'yaz':
        return 'Haziran, Temmuz, Ağustos'
    elif mevsim == 'sonbahar':
        return 'Eylül, Ekim, Kasım'
    elif mevsim == 'kış':
        return 'Aralık, Ocak, Şubat'
    else:
        return 'Böyle bir mevsim yok'
# Kullanıcıdan input alma
mevsim = input('Mevsim:  ')
print(mevsim_aylari(mevsim))



def en_buyuk_sayi(a, b, c):
    if a > b and a > c:
        return f'En büyük sayı {a}'
    elif b > a and b > c:
        return f'En büyük sayı {b}'
    elif c > a and c > b:
        return f'En büyük sayı {c}'
    else:
        return 'Sayılardan bazıları birbirine eşit'
# Kullanıcıdan input alma
a = int(input('Sayı:   '))
b = int(input('Sayı:   '))
c = int(input('Sayı:   '))

print(en_buyuk_sayi(a, b, c))



def reyon_bul(urun):
    if urun == 'elma' or urun == 'muz' or urun == 'ıspanak':
        return 'Sebze reyonuna gidiniz'
    elif urun == 'notebook' or urun == 'tablet' or urun == 'smartphone':
        return 'Teknoloji reyonuna gidiniz'
    elif urun == 'şampuan' or urun == 'sabun' or urun == 'parfüm':
        return 'Kozmetik reyonuna gidiniz'
    else:
        return 'Böyle bir ürün yok'
# Kullanıcıdan input alma
urun = input('Ürün giriniz:   ')
print(reyon_bul(urun))



def giris_yap(sifre, username):
    if sifre == 123 and username == 'basit':
        return f'{username} hoşgeldiniz'
    else:
        return 'Hatalı kullanıcı adı veya şifre'
# Kullanıcıdan input alma
sifre = int(input('Şifre: '))
username = input('Kullanıcı adı: ')
print(giris_yap(sifre, username))


def bmi_durum(boy, kilo):
    bmi = kilo / (boy ** 2)
    if 0 < bmi < 18.5:
        return 'Zayıf'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal kilolu'
    elif 25 <= bmi <= 29:
        return 'Fazla kilolu'
    elif 30 <= bmi <= 34.9:
        return 'Obez'
    elif 35 <= bmi <= 39.9:
        return 'Aşırı obez'
    elif 40 <= bmi:
        return 'Morbid obez'
    else:
        return 'Hatalı boy ya da kilo bilgisi girdiniz'
# Kullanıcıdan input alma
boy = float(input('Boy uzunluğu giriniz:   '))
kilo = float(input('Kilo değeri giriniz:   '))
print(bmi_durum(boy, kilo))



def bolme_islemi(bolen, bolunen):
    try:
        sonuc = bolunen / bolen
        return f'Sonuc: {sonuc}'
    except ZeroDivisionError as err:
        return f'Hata: {err}'
    finally:
        print('Bağlantı kapatılıyor')
# Kullanıcıdan input alma
bolen = int(input('Bolen:  '))
bolunen = int(input('Bölünen:'))
print(bolme_islemi(bolen, bolunen))


def sayac_ve_bastir():
    counter = 0
    while counter < 100:
        print(counter)
        counter += 1
# Fonksiyonu çağırma
sayac_ve_bastir()


def sayi_turlerini_say():
    sayac = 0
    ciftler = 0
    tekler = 0
    while sayac <= 100:
        if sayac % 2 == 0:
            ciftler += 1
        else:
            tekler += 1
        sayac += 1  # Her bir sayıya uğrasın diye
    print(f'Ciftler: {ciftler}\nTekler: {tekler}')
# Fonksiyonu çağırma
sayi_turlerini_say()


def sayilari_say(limit=100):
    sayac = 0
    ciftler = 0
    tekler = 0

    while sayac <= limit:
        if sayac % 2 == 0:
            ciftler += 1
        else:
            tekler += 1

        sayac += 1  # her bir sayıya uğrasın diye
        print(f'Ciftler: {ciftler}\nTekler: {tekler}')
    return ciftler, tekler
# Fonksiyonu çağırma
cift_sayisi, tek_sayisi = sayilari_say()
print(f"Toplam Çift Sayı: {cift_sayisi}, Toplam Tek Sayı: {tek_sayisi}")


def sayilarin_toplamini_hesapla(limit=100):
    sayac = 0
    ciftlerin_toplami = 0
    teklerin_toplami = 0

    while sayac <= limit:
        if sayac % 2 == 0:
            ciftlerin_toplami += sayac
        else:
            teklerin_toplami += sayac
            sayac += 1

        sayac += 1  # her bir sayıya uğrasın diye
        print(f'Cift Sayıların Toplamı: {ciftlerin_toplami}\nTek Sayıların Toplamı: {teklerin_toplami}')
    return ciftlerin_toplami, teklerin_toplami
# Fonksiyonu çağırma
cift_toplam, tek_toplam = sayilarin_toplamini_hesapla()
print(f"Toplam Çift Sayıların Toplamı: {cift_toplam}, Toplam Tek Sayıların Toplamı: {tek_toplam}")


def dort_islem():
    sayi1 = int(input('Birinci sayıyı giriniz: '))
    sayi2 = int(input('İkinci sayıyı giriniz: '))
    islem_turu = input('İşlem türünü giriniz (+, -): ')

    while islem_turu == 'e':
        if islem_turu == '+':
            print(sayi1 + sayi2)
        elif islem_turu == '-':
            print(sayi1 - sayi2)
        else:
            print('Lütfen geçerli bir işlem giriniz (+ veya -)')

        islem_turu = input('Devam etmek için "e" giriniz, çıkmak için başka bir tuşa basınız: ')
# Fonksiyonu çağırma
dort_islem()


def dort_islem():
    while True:
        islem = input("Toplama için '+', çıkarma için '-' giriniz (Çıkış için 'e' tuşlayın): ")
        if islem == 'e':
            print("Programdan çıkılıyor...")
            break
        elif islem not in ('+', '-'):
            print("Geçersiz işlem! Lütfen '+' veya '-' giriniz.")
            continue

        try:
            sayi1 = float(input("Birinci sayıyı giriniz: "))
            sayi2 = float(input("İkinci sayıyı giriniz: "))

            if islem == '+':
                sonuc = sayi1 + sayi2
                print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
            else:
                sonuc = sayi1 - sayi2
                print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
# Fonksiyonu çağırma
dort_islem()



def asal_sayi_kontrol(sayi):
    if sayi < 2:
        print(sayi, "asal değil")
        return False

    asal = True
    i = 2
    while i * i <= sayi:
        if sayi % i == 0:
            asal = False
            print('Sayı asal değil')
            break
        i += 1
    print(sayi, "asal mı?", asal)
    return asal
# Kullanıcıdan giriş alıp fonksiyonu çağırma
sayi = int(input('Sayı giriniz: '))
asal_sayi_kontrol(sayi)


def asal_sayi_sorgula():
    while True:
        sayi = int(input("Sorgulamak İstediğiniz Sayıyı Girin: "))

        if sayi % 2 == 0:
            print("Sayı asal sayı değildir.")
        else:
            print("Sayı asal sayıdır.")
            break
# Fonksiyonu çağırma
asal_sayi_sorgula()


def asal_sayi_kontrol(sayi):
    if sayi < 2:
        print('2 den küçük sayı girmeyin')
        return False
    is_prime = True
    sayac = 2
    while sayac < sayi:
        if sayi % sayac == 0:
            is_prime = False
            break
        sayac += 1  # Burada artırılmalı
    if is_prime:
        print(f'{sayi} asaldır')
    else:
        print(f'{sayi} asal değil')
    return is_prime
# Kullanıcıdan giriş alıp fonksiyonu çağırma
sayi = int(input('Sayı giriniz: '))
asal_sayi_kontrol(sayi)


def sayac_yazdir(baslangic=0, bitis=10, artis=1):
    for sayac in range(baslangic, bitis, artis):
        print(sayac, end=",")
    print()  # Yeni satır eklemek için
# Fonksiyonu çağırma
sayac_yazdir()


def sayilari_yazdir():
    for sayac in range(0, 10, 1):
        print(sayac, end=",")
    print()

    for sayac in range(10, 51, 2):
        print(sayac, end=",")
    print()

def tek_cift_sayac():
    tek_sayac = 0
    cift_sayac = 0

    for i in range(101):  # 0'dan 100'e kadar
        if i % 2 == 0:
            cift_sayac += 1
            print(f"Çift: {i}")
        else:
            tek_sayac += 1
            print(f"Tek:  {i}")

    print(f"\nToplam {tek_sayac} tek sayı ve {cift_sayac} çift sayı var.")
# Fonksiyonları çağırma
sayilari_yazdir()
tek_cift_sayac()



def sayilari_yazdir():
    for sayac in range(0, 10, 1):
        print(sayac, end=",")
    print()

    for sayac in range(10, 51, 2):
        print(sayac, end=",")
    print()



def tek_cift_sayac():
    tek_sayac = 0
    cift_sayac = 0

    for i in range(101):  # 0'dan 100'e kadar
        if i % 2 == 0:
            cift_sayac += 1
            print(f"Çift: {i}")
        else:
            tek_sayac += 1
            print(f"Tek:  {i}")

    print(f"\nToplam {tek_sayac} tek sayı ve {cift_sayac} çift sayı var.")
# Fonksiyonları çağırma
sayilari_yazdir()
tek_cift_sayac()



def kareler_yazdir(baslangic, bitis, adm_miktari):
    for i in range(baslangic, bitis + 1, adm_miktari):
        print(i ** 2, end=', ')
# Kullanıcıdan giriş alıp fonksiyonu çağırma
baslangic = int(input('Başlangıç: '))
bitis = int(input('Bitiş: '))
adm_miktari = int(input('Adım: '))
kareler_yazdir(baslangic, bitis, adm_miktari)



def carpim_tablosu():
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                print(k)
            print(f'{i} x {j} = {i * j}')
        print('==============')
# Fonksiyonu çağırma
carpim_tablosu()


def x_yazdir():
    for i in range(1, 5):  # i satır
        for j in range(1, 15):  # j sütun
            print('x', end='')
        print(' ')  # Yeni satır
# Fonksiyonu çağırma
x_yazdir()



def bosluk_yazdir():
    for i in range(1, 5):
        for j in range(1, 20):
            if j % 2 == 0:
                print('', end='')
            print(' ')  # Yeni satır
# Fonksiyonu çağırma
bosluk_yazdir()
"""