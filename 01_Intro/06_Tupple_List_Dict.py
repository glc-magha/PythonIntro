"""# 1. Tuple Kullanımı
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])  # 3

# 2. Liste Kullanımı
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print(my_list)  # [10, 20, 30, 40, 50, 60]

# 3. Dictionary Kullanımı
my_dict = {"ad": "Ali", "yas": 25}
print(my_dict["ad"])  # Ali

# 4. Slicing İşlemi
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])  # [2, 3, 4, 5, 6]

# 5. Unpacking (Paket Açma) İşlemi
a, b, c = my_tuple
print(a, b, c)  # 1 2 3

# 6. Liste İçinde Tuple
nested_list = [(1, 2), (3, 4), (5, 6)]
for x, y in nested_list:
    print(x, y)

# 7. Tuple İçinde Liste
mixed_tuple = (1, [2, 3], 4)
mixed_tuple[1].append(5)
print(mixed_tuple)  # (1, [2, 3, 5], 4)

# 8. Dictionary'den Anahtarları Alma
keys = my_dict.keys()
print(list(keys))  # ['ad', 'yas']

# 9. Slicing ile Ters Çevirme
reversed_list = numbers[::-1]
print(reversed_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 10. Dictionary'de Değer Güncelleme
my_dict["yas"] = 26
print(my_dict)  # {'ad': 'Ali', 'yas': 26}

# 11. Tuple'dan Değer Alarak Değişkenlere Atama
data = ("Ahmet", 30, "Mühendis")
name, age, job = data
print(name, age, job)  # Ahmet 30 Mühendis

# 12. Listeyi Slicing ile Parçalama
sub_list = my_list[:3]
print(sub_list)  # [10, 20, 30]

# 13. Dictionary'den Değer Silme
del my_dict["yas"]
print(my_dict)  # {'ad': 'Ali'}

# 14. Tuple'dan Liste Yapma
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # [1, 2, 3, 4, 5]

# 15. Liste Elemanlarını Tuple Yapma
list_to_tuple = tuple(my_list)
print(list_to_tuple)  # (10, 20, 30, 40, 50, 60)

# 16. Unpacking ile Değişim
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# 17. Dictionary İçinde Liste
dict_with_list = {"meyveler": ["elma", "armut", "çilek"]}
print(dict_with_list["meyveler"][1])  # armut

# 18. Liste İçinde Dictionary
list_with_dict = [{"ad": "Ali"}, {"ad": "Veli"}]
print(list_with_dict[1]["ad"])  # Veli

# 19. Slicing ile Atama
numbers[2:5] = [99, 88, 77]
print(numbers)  # [0, 1, 99, 88, 77, 5, 6, 7, 8, 9]

# 20. Dictionary'den Anahtar-Değer Çifti Alma
for key, value in my_dict.items():
    print(key, value)

# 21. Listeyi Tuple'a Çevirme
list_example = [1, 2, 3]
converted_tuple = tuple(list_example)
print(converted_tuple)  # (1, 2, 3)

# 22. Tuple İçinde Tuple
nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[1][0])  # 3

# 23. Dictionary'den Varsayılan Değerle Erişim
print(my_dict.get("soyad", "Bulunamadı"))  # Bulunamadı

# 24. Liste Dilimleme (Slicing) ile Elemanları Atla
print(numbers[::2])  # [0, 99, 77, 6, 8]

# 25. Tuple Uzunluğu
print(len(my_tuple))  # 5

# 26. Liste Elemanlarını Ayırma
first, *rest = my_list
print(first, rest)  # 10 [20, 30, 40, 50, 60]

# 27. Dictionary Kopyalama
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# 28. Tuple İçinde Farklı Tipler
mixed_tuple = (1, "Merhaba", 3.14)
print(mixed_tuple)

# 29. Listeyi Ters Çevirme
my_list.reverse()
print(my_list)

# 30. Dictionary'de Belirli Anahtar Var mı?
print("ad" in my_dict)  # True

# 31. Listeyi Tuple'a Paketleme
packed_tuple = tuple(my_list)
print(packed_tuple)

# 32. Tuple'dan Değer Çıkarma
unpacked = my_tuple[:3] + my_tuple[4:]
print(unpacked)

# 33. Dictionary'den Belirli Anahtarları Alma
keys = list(my_dict.keys())
print(keys)

# 34. Listeyi Slicing ile İkiye Bölme
mid = len(my_list) // 2
print(my_list[:mid], my_list[mid:])

# 35. Tuple'ı Döngüyle Gezinme
for item in my_tuple:
    print(item)

# 36. Listeyi Kopyalama
new_list = my_list[:]
print(new_list)

# 37. Dictionary'den Anahtar Silme
my_dict.pop("ad", None)
print(my_dict)

# 38. Listeyi Tuple Olarak Paketleme
packed_tuple = tuple(my_list)
print(packed_tuple)

# 39. Unpacking ile Çoklu Değişken Atama
x, y, z = (10, 20, 30)
print(x, y, z)

# 40. Dictionary'den Anahtarları Liste Yapma
keys_list = list(my_dict.keys())
print(keys_list)

# 41. Liste Elemanlarını Slicing ile Kopyalama
new_list = numbers[:]
print(new_list)  # [0, 1, 99, 88, 77, 5, 6, 7, 8, 9]

# 42. Tuple İçinde Tek Eleman
single_tuple = (42,)
print(single_tuple)

# 43. Dictionary'den Anahtarlar ve Değerleri Liste Yapma
items = list(my_dict.items())
print(items)

# 44. Listeyi Ters Dilimleme
print(numbers[::-1])

# 45. Unpacking ile Artan Değerler
a, *b, c = range(10)
print(a, b, c)

# 46. Tuple Elemanlarına Erişim
print(my_tuple[1])  # 2
#...................................
# 1. Tuple Kullanımı (İç İçe ve Dinamik Erişim)
complex_tuple = ((1, 2), (3, (4, 5)), (6, 7))
print(complex_tuple[1][1][0])  # 4

# 2. Liste Kullanımı (Listeyi Tek Satırda Ters Çevirip Filtreleme)
numbers = [x for x in range(20) if x % 2 == 0]
print(numbers[::-1])  # [18, 16, 14, ..., 0]

# 3. Dictionary Kullanımı (İç İçe Dictionary'den Değer Alma)
nested_dict = {"a": {"b": {"c": 42}}}
print(nested_dict["a"]["b"]["c"])  # 42

# 4. Slicing İşlemi (Çok Katmanlı Slicing)
matrix = [[i + j for j in range(5)] for i in range(5)]
print(matrix[1:4][::-1][0][1:4])  # [4, 5, 6]

# 5. Unpacking (Dinamik Uzunlukta Tuple)
data = (1, 2, 3, 4, 5, 6)
a, *middle, b = data
print(a, middle, b)  # 1 [2, 3, 4, 5] 6

# 6. Liste İçinde Tuple (Koşullu Erişim)
data = [(i, i**2) for i in range(10)]
squares = [x[1] for x in data if x[0] % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# 7. Tuple İçinde Liste (İç Listeyi Manipüle Etme)
mutable_tuple = (1, [2, 3], 4)
mutable_tuple[1][1] += 5
print(mutable_tuple)  # (1, [2, 8], 4)

# 8. Dictionary'den Anahtarları Filtreleme
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
even_keys = [k for k, v in my_dict.items() if v % 2 == 0]
print(even_keys)  # ['b', 'd']

# 9. Slicing ile Adım Adım Erişim
nums = list(range(50))
print(nums[5:30:5])  # [5, 10, 15, 20, 25]

# 10. Dictionary'de Dinamik Güncelleme
data = {"a": 1, "b": 2}
updates = [("b", 5), ("c", 10)]
for k, v in updates:
    data[k] = data.get(k, 0) + v
print(data)  # {'a': 1, 'b': 7, 'c': 10}

# 11. Tuple'dan Listeye Dönüştürme ve Manipülasyon
tup = (10, 20, 30)
lst = list(tup)
lst.insert(1, 15)
print(tuple(lst))  # (10, 15, 20, 30)

# 12. Listeyi Slicing ile Ters ve Parçalama
lst = [x**2 for x in range(10)]
print(lst[::-2])  # [81, 49, 25, 9, 1]

# 13. Dictionary'den Koşullu Anahtar Silme
data = {"x": 10, "y": 20, "z": 30}
for key in list(data.keys()):
    if data[key] > 15:
        del data[key]
print(data)  # {'x': 10}

# 14. Tuple'dan Unpacking ile Parça Alma
values = (1, 2, 3, 4, 5, 6, 7)
_, *middle, _ = values
print(middle)  # [2, 3, 4, 5, 6]

# 15. Liste ve Tuple Karışımı Yapı
complex_structure = [(x, [y for y in range(x)]) for x in range(5)]
print(complex_structure[3][1][2])  # 2

# 16. Dictionary'den Değer Alırken Varsayılan Kullanma
data = {"name": "Ali", "age": 30}
salary = data.get("salary", "Tanımsız")
print(salary)  # Tanımsız

# 17. Liste Elemanlarını Parçalama ve Ters Çevirme
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers[::-1]
print(first, middle, last)  # 5 [4, 3, 2] 1

# 18. Dictionary'de İç İçe Yapılarla Çalışma
nested_dict = {
    "person": {
        "name": "Mehmet",
        "address": {"city": "İstanbul", "zip": 34000}
    }
}
print(nested_dict["person"]["address"]["zip"])  # 34000

# 19. Tuple İçinde Listeyi Değiştirme
tup = (1, [2, 3], 4)
tup[1].extend([5, 6])
print(tup)  # (1, [2, 3, 5, 6], 4)

# 20. Listeyi Slicing ile Döngüde Kullanma
data = list(range(20))
for part in [data[i:i+5] for i in range(0, len(data), 5)]:
    print(part)
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14]
# [15, 16, 17, 18, 19]
# 21. Tuple Kullanımı (Tuple İçindeki Tuple’dan Değer Alma)
nested_tuple = ((10, 20), (30, (40, 50)), (60, 70))
print(nested_tuple[1][1][1])  # 50

# 22. Liste Kullanımı (İç İçe Listeden Değer Çekme ve Manipüle Etme)
matrix = [[x + y for y in range(3)] for x in range(3)]
matrix[2][1] = 99
print(matrix)  # [[0, 1, 2], [1, 2, 3], [2, 99, 4]]

# 23. Dictionary Kullanımı (Koşullu Değer Ekleme)
data = {"a": 5, "b": 10}
new_values = [("c", 15), ("a", 20)]
for key, value in new_values:
    data[key] = value if key not in data else data[key] + value
print(data)  # {'a': 25, 'b': 10, 'c': 15}

# 24. Slicing İşlemi (Negatif Adım ve Parçalama)
nums = list(range(10, 21))
print(nums[-2::-3])  # [19, 16, 13, 10]

# 25. Unpacking (Çok Katmanlı ve Yıldızlı Unpacking)
data = (1, (2, 3), 4, 5)
a, (b, c), *rest = data
print(a, b, c, rest)  # 1 2 3 [4, 5]

# 26. Liste İçinde Tuple (Koşullu Liste Oluşturma)
pairs = [(x, x**2) for x in range(5) if x % 2 == 1]
print(pairs)  # [(1, 1), (3, 9)]

# 27. Tuple İçinde Liste (Derin Kopyalama ve Manipülasyon)
import copy
nested_tuple = (1, [2, 3], 4)
deep_copy = copy.deepcopy(nested_tuple)
deep_copy[1].append(5)
print(nested_tuple, deep_copy)
# (1, [2, 3], 4) (1, [2, 3, 5], 4)

# 28. Dictionary'den Anahtarları Filtreleyerek Yeni Sözlük Oluşturma
data = {"x": 10, "y": 20, "z": 30}
filtered = {k: v for k, v in data.items() if v > 15}
print(filtered)  # {'y': 20, 'z': 30}

# 29. Slicing ile Karmaşık Erişim
nums = list(range(50))
print(nums[10:40:5][-2::-1])  # [30, 25, 20, 15, 10]

# 30. Dictionary'de Nested Yapıda Dinamik Erişim
data = {"a": {"b": {"c": 42}}, "x": 99}
path = ["a", "b", "c"]
result = data
for key in path:
    result = result[key]
print(result)  # 42

# 31. Liste ve Tuple Karışımı (Çift Sayıları Filtreleme)
mixed = [(i, i**2) for i in range(10)]
evens = [item for item in mixed if item[0] % 2 == 0]
print(evens)  # [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]

# 32. Unpacking ile Liste Manipülasyonu
data = [1, 2, 3, 4, 5, 6]
first, *middle, last = data
print(first, middle, last)  # 1 [2, 3, 4, 5] 6

# 33. Tuple ve Listeyi Birleştirme
tup = (1, 2, 3)
lst = [4, 5, 6]
merged = tup + tuple(lst)
print(merged)  # (1, 2, 3, 4, 5, 6)

# 34. Dictionary'den Anahtar-Value Çifti Silme ve Geri Döndürme
data = {"a": 10, "b": 20, "c": 30}
removed = data.pop("b", "Yok")
print(removed, data)  # 20 {'a': 10, 'c': 30}

# 35. Slicing ile Karmaşık Yapılar Üzerinde İşlem
matrix = [[x * y for y in range(5)] for x in range(5)]
sliced = [row[1:4] for row in matrix[1:4]]
print(sliced)  # [[0, 2, 3], [0, 3, 6], [0, 4, 8]]

# 36. Tuple İçinde Listeyi Kopyalama ve Değiştirme
original = (1, [2, 3], 4)
new = (original[0], original[1][:], original[2])
new[1].append(99)
print(original, new)
# (1, [2, 3], 4) (1, [2, 3, 99], 4)

# 37. Dictionary'den Anahtar-Value Çiftlerini Liste Yapma
data = {"name": "John", "age": 25, "city": "London"}
items_list = list(data.items())
print(items_list)
# [('name', 'John'), ('age', 25), ('city', 'London')]

# 38. Listeyi Unpacking İle Bölme
nums = [10, 20, 30, 40, 50]
a, *middle, b = nums
print(a, middle, b)  # 10 [20, 30, 40] 50

# 39. Tuple Kullanımı (İç İçe ve Dinamik Erişim)
complex_tuple = ((1, 2), (3, (4, 5)), (6, 7))
print(complex_tuple[1][1][0])  # 4

# 40. Dictionary Kullanımı (İç İçe Yapıda Dinamik Erişim ve Varsayılan Değer)
nested_dict = {"a": {"b": {"c": 42}}}
result = nested_dict.get("a", {}).get("b", {}).get("d", "Bulunamadı")
print(result)  # Bulunamadı
# 41. Liste ve Tuple Dönüşümü (İç İçe Yapılarla)
nested_list = [[1, 2], [3, 4], [5, 6]]
tupled_list = tuple(tuple(sub) for sub in nested_list)
print(tupled_list)  # ((1, 2), (3, 4), (5, 6))

# 42. Unpacking ile Değer Değişimi ve İşlem
a, b, c = 3, 6, 9
a, b, c = b + c, a * 2, b - a
print(a, b, c)  # 15, 6, 3

# 43. Dictionary İçinde Listeyi Manipüle Etme
data = {"numbers": [10, 20, 30]}
data["numbers"].append(40)
print(data)  # {'numbers': [10, 20, 30, 40]}

# 44. Slicing (Adım ile Değer Güncelleme)
numbers = list(range(20))
numbers[2:15:3] = [99] * 5
print(numbers)
# [0, 1, 99, 3, 4, 99, 6, 7, 99, 9, 10, 99, 12, 13, 99, 15, 16, 17, 18, 19]

# 45. Tuple İçinde Dictionary Kullanımı
tup_with_dict = (1, {"a": 10, "b": 20}, 3)
tup_with_dict[1]["c"] = 30
print(tup_with_dict)  # (1, {'a': 10, 'b': 20, 'c': 30}, 3)

# 46. Listeyi Tuple’a ve Tekrar Listeye Çevirme
original_list = [1, 2, 3, 4]
tuple_version = tuple(original_list)
new_list = list(tuple_version)
new_list.append(5)
print(new_list)  # [1, 2, 3, 4, 5]

# 47. Dictionary'den Anahtar Kontrolü (Koşullu Ekleme)
inventory = {"elma": 5, "armut": 3}
if "muz" not in inventory:
    inventory["muz"] = 10
print(inventory)  # {'elma': 5, 'armut': 3, 'muz': 10}

# 48. Unpacking (Liste İçinde Liste Yapısında)
nested_list = [1, [2, 3, 4], 5]
a, (b, *c), d = nested_list
print(a, b, c, d)  # 1 2 [3, 4] 5

# 49. Slicing ile Ters Çevir ve Kopyala
original = list(range(10))
reversed_copy = original[::-1]
print(reversed_copy)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 50. Dictionary'de Koşullu Silme
grades = {"Ahmet": 85, "Ayşe": 90, "Ali": 70}
for key in list(grades.keys()):
    if grades[key] < 80:
        del grades[key]
print(grades)  # {'Ayşe': 90}

# 51. Liste İçinde Tuple ve Eleman Erişimi
data = [(i, i**2, i**3) for i in range(5)]
print(data[3][2])  # 27

# 52. Tuple'dan Değer Sıkıştırma (Slicing ve Toplama)
my_tuple = (10, 20, 30, 40, 50)
compressed = my_tuple[:2] + my_tuple[-2:]
print(compressed)  # (10, 20, 40, 50)

# 53. Dictionary ve Liste Kombinasyonu
students = {"Ali": [85, 90], "Ayşe": [78, 92]}
students["Veli"] = [88, 77]
print(students["Veli"][1])  # 77

# 54. Unpacking ile Eleman Atama (İç İçe Yapılarla)
data = (1, [2, (3, 4)], 5)
a, [b, (c, d)], e = data
print(a, b, c, d, e)  # 1 2 3 4 5

# 55. Listeyi Parçalayarak (Slicing) Elemanları Ayırma
numbers = list(range(10))
first_half, second_half = numbers[:5], numbers[5:]
print(first_half, second_half)  # [0, 1, 2, 3, 4] [5, 6, 7, 8, 9]

# 56. Dictionary'de Dinamik Değer Ekleme (get Kullanımı)
data = {"x": 100}
data["y"] = data.get("y", 50) + 25
print(data)  # {'x': 100, 'y': 75}

# 57. Tuple İçinde Listeyi Değiştir (Derin Kopya Kullanımı)
import copy
original = (1, [2, 3], 4)
new_version = copy.deepcopy(original)
new_version[1].append(5)
print(original, new_version)
# (1, [2, 3], 4) (1, [2, 3, 5], 4)

# 58. Unpacking ile Karışık Yapıları Ayırma
data = [(1, 2), (3, 4), (5, (6, 7))]
for a, b in data:
    if isinstance(b, tuple):
        print(a, *b)  # 5 6 7

# 59. Liste ve Dictionary Yapısını Karıştırma
data = [{"ad": "Ahmet", "notlar": [85, 90]}, {"ad": "Ayşe", "notlar": [78, 82]}]
for item in data:
    item["notlar"].append(95)
print(data)
# [{'ad': 'Ahmet', 'notlar': [85, 90, 95]}, {'ad': 'Ayşe', 'notlar': [78, 82, 95]}]

# 60. Slicing ile Kopyalama ve Manipülasyon
numbers = list(range(1, 11))
numbers[1:8:2] = [99] * 4
print(numbers)
# [1, 99, 3, 99, 5, 99, 7, 99, 9, 10]
#1. List comprehension kullanarak bir sayı listesinde sadece çift sayıları nasıl seçersiniz?

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
#2. Bir string içindeki sesli harfleri saymak için bir fonksiyon yazın.

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("hello world"))
#3. Bir sayının asal olup olmadığını kontrol eden bir fonksiyon yazın.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(11))
#4. Bir listeyi tersine çevirecek bir fonksiyon yazın.

def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))
#5. Bir listede tekrar eden elemanları nasıl bulabilirsiniz?

def find_duplicates(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

print(find_duplicates([1, 2, 3, 4, 4, 5, 6, 7, 7]))
#6. Bir dizideki en büyük ve en küçük sayıyı nasıl bulursunuz?

numbers = [1, 2, 3, 4, 5, 6]
print("En büyük sayı:", max(numbers))
print("En küçük sayı:", min(numbers))
#7. Bir string’in tüm harflerinin küçük harfe dönüştürülmesi için bir fonksiyon yazın.

def to_lower_case(s):
    return s.lower()

print(to_lower_case("Hello WORLD"))
#8. Bir listeyi sıralamak için Python’un yerleşik sorted() fonksiyonunu kullanmadan nasıl sıralarsınız?

def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(custom_sort([3, 1, 4, 5, 2]))
#9. Bir listede en fazla tekrar eden öğeyi bulun.

from collections import Counter

def most_common(lst):
    counter = Counter(lst)
    return counter.most_common(1)[0][0]

print(most_common([1, 2, 3, 3, 4, 5, 3]))
#10. Bir stringdeki boşlukları kaldırmak için bir fonksiyon yazın.

def remove_spaces(s):
    return s.replace(" ", "")

print(remove_spaces("hello world"))
#11. Bir sayının faktoriyelini hesaplayan bir fonksiyon yazın.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
#12. Bir listeyi çift ve tek olmak üzere iki ayrı listeye ayırın.

def split_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

print(split_even_odd([1, 2, 3, 4, 5, 6]))
#13. Bir string’i palindrom olup olmadığını kontrol eden bir fonksiyon yazın.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
#14. Bir listeyi birleştirerek bir string’e dönüştürün.

def list_to_string(lst):
    return ''.join(map(str, lst))

print(list_to_string([1, 2, 3, 4]))
#15. Bir kelimenin harflerinden her biri için bir sayıyı temsil eden bir sözlük yazın.

def letter_to_number(s):
    return {char: ord(char) for char in s}

print(letter_to_number("hello"))
#16. Bir sayının tek mi çift mi olduğunu belirlemek için bir fonksiyon yazın.

def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(is_even_or_odd(5))
#17. Bir dizinin toplamını hesaplayan bir fonksiyon yazın.

def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))
#18. Bir sayının tüm pozitif bölenlerini bulan bir fonksiyon yazın.

def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(find_divisors(12))
#19. Bir string'in her harfiyle başladığı bir fonksiyon yazın.

def starts_with_each_char(s):
    return [s.startswith(char) for char in s]

print(starts_with_each_char("hello"))
#20. Bir listede yer alan her öğeyi iki katına çıkaracak bir fonksiyon yazın.

def double_elements(lst):
    return [x * 2 for x in lst]

print(double_elements([1, 2, 3, 4]))
#21. Bir sayıyı binary formatta yazdıran bir fonksiyon yazın.

def to_binary(n):
    return bin(n)[2:]

print(to_binary(10))
#22. Bir sayının karesini alacak bir fonksiyon yazın.

def square(n):
    return n ** 2

print(square(5))
#23. Bir sayının tam sayı olup olmadığını kontrol eden bir fonksiyon yazın.

def is_integer(n):
    return isinstance(n, int)

print(is_integer(4))
#24. Bir listede pozitif ve negatif sayıları ayıran bir fonksiyon yazın.

def separate_signs(lst):
    positive = [x for x in lst if x > 0]
    negative = [x for x in lst if x < 0]
    return positive, negative

print(separate_signs([-1, 2, -3, 4, 5]))
#25. Bir string’i tersine çeviren bir fonksiyon yazın.

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
#26. Bir sayı listesinde en fazla tekrar eden sayıyı bulmak için bir fonksiyon yazın.

from collections import Counter

def most_frequent(lst):
    counter = Counter(lst)
    return counter.most_common(1)[0][0]

print(most_frequent([1, 2, 3, 3, 4, 5, 3]))
#27. Bir listeyi sadece string türündeki öğeleriyle filtreleyin.

def filter_strings(lst):
    return [x for x in lst if isinstance(x, str)]

print(filter_strings([1, "apple", 3, "banana", 5]))
#28. Bir dizide yalnızca tek sayıları seçmek için bir fonksiyon yazın.

def filter_odd(lst):
    return [x for x in lst if x % 2 != 0]

print(filter_odd([1, 2, 3, 4, 5]))
#29. Bir listeyi enumerate() ile her elemanını numaralandırarak yazdırın.

lst = ["apple", "banana", "cherry"]
for idx, value in enumerate(lst):
    print(f"{idx}: {value}")
#30. Bir sayı listesinde, tüm elemanların karelerinin toplamını bulan bir fonksiyon yazın.

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

print(sum_of_squares([1, 2, 3, 4]))
#31. Bir dizide tüm benzersiz öğeleri birleştiren bir fonksiyon yazın.

def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 2, 3, 3, 4]))
#32. Bir sayıyı rakamlara ayıran bir fonksiyon yazın.

def split_digits(n):
    return [int(digit) for digit in str(n)]

print(split_digits(12345))
#33. Bir string’in her kelimesinin ilk harfini büyük yapın.

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_words("hello world"))
#34. Bir string'i harflerine göre sıralayacak bir fonksiyon yazın.

def sort_string(s):
    return ''.join(sorted(s))

print(sort_string("hello"))
#35. Bir diziyi, her öğesinin karesiyle değiştiren bir fonksiyon yazın.

def square_elements(lst):
    return [x ** 2 for x in lst]

print(square_elements([1, 2, 3, 4]))
#36. Bir listeyi set kullanarak benzersiz hale getiren bir fonksiyon yazın.

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))
#37. Bir string’in tüm harflerini sıralayan bir fonksiyon yazın.

def sort_letters(s):
    return ''.join(sorted(s))

print(sort_letters("hello"))
#38. Bir dizinin ortalama değerini bulan bir fonksiyon yazın.

def average(lst):
    return sum(lst) / len(lst)

print(average([1, 2, 3, 4, 5]))
#39. Bir string içindeki her kelimenin baş harfini büyük yapacak bir fonksiyon yazın.

def capitalize_first_letters(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_first_letters("hello world"))
#40. Bir sayının, 1’den kendisine kadar olan sayıların toplamına eşit olup olmadığını kontrol eden bir fonksiyon yazın.

def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

print(is_perfect_number(28))
#41. Bir dizideki tüm elemanları pozitif hale getiren bir fonksiyon yazın.

def make_positive(lst):
    return [abs(x) for x in lst]

print(make_positive([-1, 2, -3, 4]))
#42. Bir dizinin ilk n elemanını yazdıracak bir fonksiyon yazın.

def first_n_elements(lst, n):
    return lst[:n]

print(first_n_elements([1, 2, 3, 4, 5], 3))
#43. Bir string içindeki en fazla tekrar eden harfi bulun.

from collections import Counter

def most_frequent_char(s):
    counter = Counter(s)
    return counter.most_common(1)[0][0]

print(most_frequent_char("hello world"))
#44. Bir listede yer alan sayılara ait kare köklerini hesaplayan bir fonksiyon yazın.

import math

def square_roots(lst):
    return [math.sqrt(x) for x in lst]

print(square_roots([1, 4, 9, 16]))
#45. Bir sayının asal olup olmadığını kontrol eden fonksiyonun, optimize edilmiş halini yazın.

def optimized_is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(optimized_is_prime(29))
#46. Bir dizinin toplamının, bir sayıya bölünüp bölünmediğini kontrol eden bir fonksiyon yazın.

def is_divisible(lst, num):
    return sum(lst) % num == 0

print(is_divisible([1, 2, 3, 4], 10))
#47. Bir dizinin elemanlarını büyük harfe dönüştürüp yazdıracak bir fonksiyon yazın.

def capitalize_elements(lst):
    return [str(x).upper() for x in lst]

print(capitalize_elements(["apple", "banana", "cherry"]))
#48. Bir sayıyı Fibonacci dizisindeki karşılık gelen sayıya dönüştüren bir fonksiyon yazın.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(7))
#49. Bir dizinin tersini yazdıran bir fonksiyon yazın, ancak reverse() veya [::-1] kullanmayın.

def reverse_list_manually(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result

print(reverse_list_manually([1, 2, 3, 4, 5]))
#. Bir string içindeki her harfi, ASCII değerine dönüştüren bir fonksiyon yazın.

def string_to_ascii(s):
    return [ord(char) for char in s]

print(string_to_ascii("hello"))
#................................................
# Tuple Unpacking ve slicing örneği
def process_data(data):
    # Veriyi unpack etmek
    (a, b, c, *rest) = data
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"Diğer elemanlar: {rest}")


# Test
data = (1, 2, 3, 4, 5, 6)
process_data(data)


# List slicing ve dictionary comprehension
def generate_dict_from_list(lst):
    return {x: x ** 2 for x in lst[:5]}  # İlk 5 elemandan sözlük oluştur


# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(generate_dict_from_list(numbers))
# Tuple içinde liste ve tuple karmaşıklığı
data = [(1, [2, 3]), (4, [5, 6])]
processed = [(a, [b*2 for b in lst]) for a, lst in data]
print(processed)

# Tuple içinde liste ve tuple karmaşıklığı
data = [(1, [2, 3]), (4, [5, 6])]
processed = [(a, [b*2 for b in lst]) for a, lst in data]
print(processed)
# Nested dictionary ve recursive unpacking
def recursive_unpack(d):
    if isinstance(d, dict):
        for key, value in d.items():
            print(f"{key}: {value}")
            recursive_unpack(value)  # Eğer değer bir dict ise tekrar unpack yap

nested_dict = {
    'a': {
        'b': {'c': 1, 'd': 2},
        'e': 3
    },
    'f': 4
}

recursive_unpack(nested_dict)
# List comprehension ve dictionary unpacking
def process_dict(d):
    return [f"{key}: {value}" for key, value in d.items() if isinstance(value, int)]

# Test
my_dict = {'name': 'John', 'age': 30, 'location': 'NYC'}
print(process_dict(my_dict))
import copy

# Mutable ve Immutable tiplerin farklı davranışı
original_dict = {
    'a': [1, 2, 3],
    'b': (4, 5, 6)
}

# Shallow copy
shallow_copy = copy.copy(original_dict)
shallow_copy['a'].append(4)

# Deep copy
deep_copy = copy.deepcopy(original_dict)
deep_copy['a'].append(4)

print("Original Dict:", original_dict)  # Shallow copy nedeniyle orijinal dict değişir
print("Shallow Copy:", shallow_copy)    # Shallow copy değişmiş
print("Deep Copy:", deep_copy)          # Deep copy etkilenmez
from functools import reduce

# Lambda, map, filter, reduce kullanımı
numbers = [1, 2, 3, 4, 5, 6]

# Her sayının karesini almak (map)
squared = list(map(lambda x: x**2, numbers))

# 10'dan büyük olan sayıları filtrelemek (filter)
greater_than_ten = list(filter(lambda x: x > 10, squared))

# Liste elemanlarını çarparak tek bir sonuç elde etmek (reduce)
product = reduce(lambda x, y: x * y, greater_than_ten)

print("Squared:", squared)
print("Greater than 10:", greater_than_ten)
print("Product of elements:", product)
# Generator kullanımı
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

# Generator ile Fibonacci dizisi oluşturma
gen = fibonacci(10)
for num in gen:
    print(num)
import time

# Basit dekoratör
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done!"

# Test
print(slow_function())
# List, Set ve Dictionary birleştirme
list_data = [1, 2, 3, 4]
set_data = {3, 4, 5, 6}
dict_data = {'a': 1, 'b': 2, 'c': 3}

# Listeyi set ile birleştir (benzersiz elemanlar)
combined_set = set(list_data).union(set_data)
print("Combined Set:", combined_set)

# List ve dict'i birleştir
combined_dict = {key: value for key, value in zip(list_data, dict_data.values())}
print("Combined Dictionary:", combined_dict)
# Set ve dictionary comprehension örneği
numbers = [1, 2, 3, 4, 5]

# Set comprehension
squares_set = {x**2 for x in numbers}
print("Squares Set:", squares_set)

# Dictionary comprehension
squares_dict = {x: x**2 for x in numbers}
print("Squares Dictionary:", squares_dict)
# Basit metaclass örneği
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['class_name'] = name  # Her sınıfa class_name ekle
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.class_name)  # MyClass


# Context Manager örneği
class MyContextManager:
    def __enter__(self):
        print("Başlangıç: Kaynak açıldı.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Bitiş: Kaynak kapatıldı.")
        if exc_type:
            print(f"Hata: {exc_value}")
        return True  # Hata varsa exception'ı yutar


# with bloğu ile kullanımı
with MyContextManager() as manager:
    print("İşlem yapılıyor...")
    # raise ValueError("Test error")  # Hata fırlatmak için açabilirsiniz


# Custom iterator ve iterable sınıfı
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# Test
rev = Reverse('giraffe')
for char in rev:
    print(char)
# Memoization (cache) ile Fibonacci hesaplama
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print(fibonacci(10))  # Çok hızlı bir şekilde hesaplanır
import asyncio

# Asenkron fonksiyon
async def fetch_data():
    print("Veri çekiliyor...")
    await asyncio.sleep(2)  # Simüle edilmiş I/O işlemi
    print("Veri çekildi!")

# Asenkron main fonksiyonunu çalıştırmak
async def main():
    await fetch_data()

# Test
asyncio.run(main())
# Multiple inheritance ve MRO
class A:
    def speak(self):
        print("A sınıfından selam")

class B:
    def speak(self):
        print("B sınıfından selam")

class C(A, B):
    pass

# Test
c = C()
c.speak()  # A sınıfı önce gelir, çünkü A, B'den önce listelenmiş
print(C.mro())  # MRO'yu yazdır
from collections import namedtuple

# NamedTuple kullanımı
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)

print(f"X: {p.x}, Y: {p.y}")

# Type hinting örneği
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))  # 5
from abc import ABC, abstractmethod


# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2


# Test
circle = Circle(5)
print(circle.area())  # 78.5
# Singleton pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True, aynı örnek

"""