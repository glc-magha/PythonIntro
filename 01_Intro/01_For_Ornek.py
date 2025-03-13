"""#1'den 10'a kadar olan sayıları yazdırma:
for i in range(1, 11):
    print(i)

#10'dan 1'e kadar olan sayıları yazdırma:
for i in range(10, 0, -1):
    print(i)

#Çift sayıları yazdırma (1-20 arası):
for i in range(2, 21, 2):
    print(i)

#Tek sayıları yazdırma (1-20 arası):
for i in range(1, 21, 2):
    print(i)

#5'in katlarını yazdırma (1-50 arası):
for i in range(5, 51, 5):
    print(i)


#Bir listeyi yazdırma
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


#Bir dizinin her elemanına 2 ekleyip yazdırma:
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number + 2)


#Bir dizinin her elemanını ikiyle çarpma:
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number * 2)

#Bir dizinin her elemanını büyük harfle yazdırma:
words = ['hello', 'world']
for word in words:
    print(word.upper())

#Bir dizinin her elemanını küçük harfle yazdırma:
words = ['HELLO', 'WORLD']
for word in words:
    print(word.lower())

#1'den 10'a kadar olan sayıların karesini yazdırma:
for i in range(1, 11):
    print(i**2)

#Bir dizideki elemanların toplamını bulma:
numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total += number
print(total)


#Bir dizideki en büyük sayıyı bulma:
numbers = [1, 2, 3, 4, 10, 6]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)


#Bir dizideki en küçük sayıyı bulma:
numbers = [1, 2, 3, 4, 10, 6]
min_num = numbers[0]
for number in numbers:
    if number < min_num:
        min_num = number
print(min_num)


#1'den 100'e kadar olan sayıların toplamını hesaplama:
total = 0
for i in range(1, 101):
    total += i
print(total)


#Bir dizinin elemanlarının sayısını bulma:
items = ['apple', 'banana', 'cherry']
count = 0
for item in items:
    count += 1
print(count)


#Her elemanın 3 katını yazdırma:
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number * 3)


#Bir dizedeki her harfi yazdırma:
word = "hello"
for letter in word:
    print(letter)


#Bir dizideki tüm harflerin ASCII değerlerini yazdırma:
word = "hello"
for letter in word:
    print(ord(letter))

#Bir dizedeki her harfi ters sırayla yazdırma
word = "hello"
for letter in word[::-1]:
    print(letter)


#Bir listeyi ters çevirmeden yazdırma:
numbers = [1, 2, 3, 4]
for number in numbers[::-1]:
    print(number)


#1 ile 10 arasında bir sayı ve bir listeyi birleştirip yazdırma:
numbers = [10, 20, 30]
for i in range(1, 11):
    print(i, numbers)


#Sayıların faktöriyelini hesaplama:
for i in range(1, 6):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print(f"Faktoriyel({i}): {factorial}")

#Bir dizideki çift sayıları seçme:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for number in numbers:
    if number % 2 == 0:
        print(number)

#Bir dizideki tek sayıları seçme:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for number in numbers:
    if number % 2 != 0:
        print(number)


#Bir dizinin her elemanını sırasıyla yazdırma:
items = [5, 10, 15]
for item in items:
    print(item)


#Bir dizideki sayılara 10 ekleyip yazdırma:
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number + 10)


#Bir sayının asal olup olmadığını kontrol etme:
num = 29
for i in range(2, num):
    if num % i == 0:
        print(f"{num} asal değildir.")
        break
else:
    print(f"{num} asal bir sayıdır.")


#Bir dizideki her harfi iki kez yazdırma:
word = "hello"
for letter in word:
    print(letter * 2)


#1 ile 20 arasındaki sayılardan 3'e bölünebilenleri yazdırma:
for i in range(1, 21):
    if i % 3 == 0:
        print(i)


#1 ile 100 arasındaki sayıların 4'e bölümünden kalanları yazdırma:
for i in range(1, 101):
    print(i % 4)


#Bir dizinin her elemanını iki katına çıkarmak ve yazdırmak:
numbers = [2, 4, 6]
for number in numbers:
    print(number * 2)


#Bir kelimeyi tersten yazdırma:
word = "example"
for letter in word[::-1]:
    print(letter, end="")

#Bir dizinin elemanlarını sırasıyla 2 kez yazdırma:
numbers = [1, 2, 3]
for number in numbers:
    print(number)
    print(number)


#Bir sayı dizisinin toplamını bulma:
numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total += number
print("Toplam:", total)


#Bir kelimenin her harfini ASCII koduna dönüştürme:
word = "hello"
for letter in word:
    print(ord(letter))


#1'den 50'ye kadar olan sayılardan 5'in katlarını yazdırma:
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

#Bir listede bulunan her elemanın uzunluğunu yazdırma:
words = ['apple', 'banana', 'cherry']
for word in words:
    print(len(word))


#Bir diziyi ters çevirip yazdırma:
numbers = [1, 2, 3, 4]
for number in reversed(numbers):
    print(number)


#Bir dizinin her elemanını 3 kez yazdırma:
items = ['a', 'b', 'c']
for item in items:
    print(item * 3)

"""