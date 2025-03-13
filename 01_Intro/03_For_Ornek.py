"""#  1'den 10'a kadar sayıları yazdır
for i in range(1, 11):
    print(i)

#  Listeden elemanları yazdır
meyveler = ["Elma", "Armut", "Muz"]
for meyve in meyveler:
    print(meyve)

#  2'şer artarak 20'ye kadar sayıları yazdır
for i in range(0, 21, 2):
    print(i)

#  Bir kelimenin harflerini yazdır
kelime = "Python"
for harf in kelime:
    print(harf)

# 1'den 100'e kadar olan sayıların toplamını hesapla
toplam = 0
for i in range(1, 101):
    toplam += i
print("Toplam:", toplam)

#  Çift sayıları filtrele
sayılar = [10, 15, 22, 33, 42, 55]
for sayı in sayılar:
    if sayı % 2 == 0:
        print(sayı)

#  5x5 yıldız matrisi yazdır
for _ in range(5):
    print("*" * 5)

#  İç içe döngü ile çarpım tablosu
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")

#  Bir listenin elemanlarını ters sırayla yazdır
liste = [1, 2, 3, 4, 5]
for eleman in reversed(liste):
    print(eleman)

#  1'den 10'a kadar olan sayıların karelerini yazdır
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")

#  Bir stringde kaç tane "a" harfi olduğunu bul
kelime = "Ankara'nın bağları"
sayac = 0
for harf in kelime:
    if harf == "a":
        sayac += 1
print("A harfi sayısı:", sayac)

#  Liste içindeki en büyük sayıyı bul
sayılar = [15, 22, 8, 37, 49, 50]
maks = sayılar[0]
for sayı in sayılar:
    if sayı > maks:
        maks = sayı
print("En büyük sayı:", maks)

#  Bir listeyi index numarasıyla birlikte yazdır
renkler = ["Kırmızı", "Mavi", "Yeşil"]
for index, renk in enumerate(renkler):
    print(f"{index}: {renk}")

#  Bir set içindeki elemanları yazdır
renkler = {"Kırmızı", "Yeşil", "Mavi"}
for renk in renkler:
    print(renk)

#  Faktöriyel hesaplama
faktöriyel = 1
n = 5
for i in range(1, n + 1):
    faktöriyel *= i
print(f"{n}! = {faktöriyel}")

#  1-100 arasındaki asal sayıları bul
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

#  Ters üçgen oluşturma
for i in range(5, 0, -1):
    print("*" * i)

# Fibonacci serisi (10 eleman)
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

#  Liste içindeki çift sayıları ve tek sayıları ayır
sayılar = [1, 2, 3, 4, 5, 6]
ciftler = [sayı for sayı in sayılar if sayı % 2 == 0]
tekler = [sayı for sayı in sayılar if sayı % 2 != 0]
print("Çiftler:", ciftler)
print("Tekler:", tekler)

#  Ters string oluşturma
kelime = "Python"
ters_kelime = ""
for harf in kelime:
    ters_kelime = harf + ters_kelime
print("Ters:", ters_kelime)



#  1'den 10'a kadar yazdır
i = 1
while i <= 10:
    print(i)
    i += 1

# Kullanıcı "exit" girene kadar giriş al
girdi = ""
while girdi != "exit":
    girdi = input("Komut gir: ")

#  Rastgele bir sayı tahmin etme oyunu
import random
sayı = random.randint(1, 10)
tahmin = 0
while tahmin != sayı:
    tahmin = int(input("Tahmin gir: "))
print("Doğru tahmin!")

# 24. Sonsuz döngü
while True:
    print("Bu sonsuz döngü!")

# Kullanıcıdan 0 girene kadar sayı al ve topla
toplam = 0
while True:
    sayı = int(input("Sayı gir (0 çıkış): "))
    if sayı == 0:
        break
    toplam += sayı
print("Toplam:", toplam)

#  1-100 arasındaki çift sayıları yazdır
i = 2
while i <= 100:
    print(i)
    i += 2

#  5! faktöriyel hesapla
n = 5
faktöriyel = 1
while n > 0:
    faktöriyel *= n
    n -= 1
print("5! =", faktöriyel)

#  Fibonacci serisi (while ile)
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#  Sayının basamaklarını toplama
sayı = 1234
toplam = 0
while sayı > 0:
    toplam += sayı % 10
    sayı //= 10
print("Basamak toplamı:", toplam)

# Sayının asal olup olmadığını bulma
n = 29
i = 2
asal = True
while i < n:
    if n % i == 0:
        asal = False
        break
    i += 1
print(n, "asal mı?", asal)




i = 10
while i > 0:
    print(i)
    i -= 1

toplam = 0
i = 1

while i <= 10:
    toplam += i
    i += 1
print("Toplam:", toplam)

kelime = "Python"
i = 0

while i < len(kelime):
    print(kelime[i])
    i += 1



#  Liste içindeki sayıların karelerini yeni bir listeye ekleyerek yazdır
sayılar = [1, 2, 3, 4, 5]
kareler = [sayı**2 for sayı in sayılar]
print(kareler)


#  1 ile 100 arasındaki 3 ve 5’e bölünebilen sayıları yazdır
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


#  String içinde belirli bir harfi değiştir
kelime = "Merhaba"
yeni_kelime = ""
for harf in kelime:
    if harf == "a":
        yeni_kelime += "@"
    else:
        yeni_kelime += harf
print(yeni_kelime)


#  Satırlı yıldız deseni çiz
for i in range(1, 6):
    print("*" * i)

#İç içe `for` döngüsü ile 3x3 matris oluştur
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

#
#  Liste elemanlarını ters sırayla yazdır (tersten sıralama)
renkler = ["Mavi", "Yeşil", "Kırmızı"]
for renk in renkler[::-1]:
    print(renk)

#İç içe döngü ile satranç tahtası oluştur
for i in range(8):
    for j in range(8):
        print("⬛" if (i + j) % 2 == 0 else "⬜", end=" ")
    print()

#  Büyük harfleri küçük harfe çevir ve tersi
kelime = "PyThOn"
yeni_kelime = ""
for harf in kelime:
    yeni_kelime += harf.lower() if harf.isupper() else harf.upper()
print(yeni_kelime)

#  Bir listeyi sıralama algoritması (bubble sort)
sayılar = [5, 2, 9, 1, 6]
for i in range(len(sayılar) - 1):
    for j in range(len(sayılar) - i - 1):
        if sayılar[j] > sayılar[j + 1]:
            sayılar[j], sayılar[j + 1] = sayılar[j + 1], sayılar[j]
print(sayılar)

#  İç içe `for` ile Pascal Üçgeni oluştur
satır_sayısı = 5
for i in range(satır_sayısı):
    sayı = 1
    for j in range(i + 1):
        print(sayı, end=" ")
        sayı = sayı * (i - j) // (j + 1)
    print()

"""