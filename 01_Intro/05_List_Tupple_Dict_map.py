"""# 1. 1'den 10'a kadar sayıların karesini listeye alma
squares = [x**2 for x in range(1, 11)]

# 2. 1'den 10'a kadar tek sayıları listeye alma
odds = [x for x in range(1, 11) if x % 2 != 0]

# 3. 1'den 10'a kadar çift sayıları listeye alma
evens = [x for x in range(1, 11) if x % 2 == 0]

# 4. Bir string'deki sesli harfleri çıkarma
text = "Python List Comprehension"
vowels = [char for char in text if char.lower() in 'aeiou']

# 5. 5'e bölünebilen sayıları listeye alma
divisible_by_5 = [x for x in range(1, 51) if x % 5 == 0]

# 6. Çift sayıların karesini hesaplama
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]

# 7. Çift sayıları çift, tekleri tek olarak listeleme
parity = ["Çift" if x % 2 == 0 else "Tek" for x in range(1, 11)]

# 8. String listeyi büyük harfe çevirme
words = ["python", "list", "comprehension"]
uppercase_words = [word.upper() for word in words]

# 9. Çift index'teki elemanları alma
numbers = [10, 20, 30, 40, 50, 60]
even_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]

# 10. Çift sayıları "Çift", tek sayıları "Tek" olarak listeleme
number_labels = ["Çift" if x % 2 == 0 else "Tek" for x in range(10)]
# 11. Tuple oluşturma
t = (1, 2, 3, 4, 5)

# 12. Tuple unpacking
a, b, c = (10, 20, 30)

# 13. Tuple elemanlarına erişim
t = (5, 10, 15)
print(t[0])  # 5

# 14. Tuple birleştirme
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2

# 15. Tuple içinde tuple kullanımı
nested_tuple = ((1, 2, 3), (4, 5, 6))

# 16. Tuple'dan listeye çevirme
t = (1, 2, 3, 4)
lst = list(t)

# 17. Tuple uzunluğunu alma
length = len((1, 2, 3, 4, 5))

# 18. Bir elemanın tuple içinde olup olmadığını kontrol etme
exists = 3 in (1, 2, 3, 4, 5)

# 19. Tuple içinde maksimum ve minimum bulma
nums = (10, 50, 30, 20)
maximum = max(nums)
minimum = min(nums)

# 20. Tuple elemanlarını sıralama
sorted_tuple = tuple(sorted((5, 2, 8, 1)))
# 21. Dictionary oluşturma
d = {"name": "Ali", "age": 25}

# 22. Dictionary elemanlarına erişim
print(d["name"])  # "Ali"

# 23. Dictionary'e yeni eleman ekleme
d["city"] = "Istanbul"

# 24. Dictionary elemanlarını listeleme
keys = list(d.keys())
values = list(d.values())

# 25. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

# 26. Dictionary içindeki değerleri değiştirme
d["age"] += 1

# 27. Dictionary elemanlarını silme
del d["city"]

# 28. Key olup olmadığını kontrol etme
exists = "name" in d

# 29. Default değer ile get kullanımı
age = d.get("age", "Bilinmiyor")

# 30. Dictionary elemanlarını dolaşma
for key, value in d.items():
    print(f"{key}: {value}")
# 31. Liste elemanlarını karesini alma
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

# 32. String uzunluklarını alma
words = ["Python", "Map", "Function"]
lengths = list(map(len, words))

# 33. İki listenin elemanlarını toplama
a = [1, 2, 3]
b = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, a, b))

# 34. Sayıları string'e çevirme
numbers = [10, 20, 30]
str_numbers = list(map(str, numbers))

# 35. Fahrenheit'ı Celsius'a çevirme
fahrenheit = [32, 68, 100]
celsius = list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))
# 36. Lambda ile toplama
add = lambda x, y: x + y

# 37. Lambda ile çarpma
multiply = lambda x, y: x * y

# 38. Lambda ile kare alma
square = lambda x: x**2

# 39. Lambda ile çift sayı kontrolü
is_even = lambda x: x % 2 == 0

# 40. Lambda ile liste filtreleme
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 41. Lambda ile string uzunluğunu ölçme
length = lambda s: len(s)

# 42. Lambda ile büyük-küçük harf dönüşümü
to_upper = lambda s: s.upper()

# 43. Lambda ile sıralama kriteri belirleme
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))

# 44. Lambda ile maksimum bulma
max_value = max(numbers, key=lambda x: x)

# 45. Lambda ile liste elemanlarını tersine çevirme
reverse_string = lambda s: s[::-1]
# 46. List comprehension ve map birlikte
squared = list(map(lambda x: x**2, [x for x in range(1, 6)]))

# 47. Dictionary comprehension ve lambda
double_values = {k: v*2 for k, v in {"a": 1, "b": 2}.items()}

# 48. Tuple ve map kullanımı
t = (1, 2, 3)
new_t = tuple(map(lambda x: x**2, t))

# 49. List comprehension, dictionary ve lambda bir arada
d = {x: (lambda y: y**2)(x) for x in range(1, 6)}

# 50. Lambda, map ve filter bir arada
filtered_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
# 51. Bir listenin elemanlarını ters çevirme
reversed_list = [x for x in reversed([1, 2, 3, 4, 5])]

# 52. 1'den 100'e kadar asal sayıları listeye alma
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

# 53. İç içe list comprehension kullanarak matris oluşturma
matrix = [[j for j in range(5)] for i in range(3)]

# 54. String içindeki harfleri ASCII koduna çevirme
ascii_values = [ord(char) for char in "Python"]

# 55. Büyük harfleri listeye alma
uppercase_chars = [char for char in "PyThoN" if char.isupper()]
# 56. Bir tuple içindeki string'lerin uzunluklarını hesaplama
words_tuple = ("apple", "banana", "cherry")
lengths_tuple = tuple(map(len, words_tuple))

# 57. Tuple'dan belirli elemanları filtreleme
numbers_tuple = (10, 15, 20, 25, 30)
even_numbers_tuple = tuple(x for x in numbers_tuple if x % 2 == 0)

# 58. Tuple içindeki elemanları swap etme
a, b = (5, 10)
a, b = b, a  # a=10, b=5

# 59. Tuple içindeki tüm elemanları toplama
sum_tuple = sum((1, 2, 3, 4, 5))

# 60. İç içe tuple ile öğrenci bilgileri saklama
students = (("Ali", 23, "Math"), ("Ayşe", 22, "Physics"))
# 61. Dictionary içindeki tüm değerleri karesiyle değiştirme
nums_dict = {"a": 2, "b": 3, "c": 4}
squared_dict = {k: v**2 for k, v in nums_dict.items()}

# 62. Dictionary'deki en büyük değeri bulma
max_value = max(nums_dict.values())

# 63. Dictionary'deki anahtarları alfabetik sıralama
sorted_keys = sorted(nums_dict.keys())

# 64. Dictionary'de belirli bir değeri olan anahtarları alma
filtered_keys = [k for k, v in nums_dict.items() if v > 2]

# 65. Dictionary içinde iç içe dictionary kullanımı
nested_dict = {"student1": {"name": "Ali", "age": 22}, "student2": {"name": "Ayşe", "age": 23}}
# 66. Map ile kelimeleri ters çevirme
words = ["hello", "world"]
reversed_words = list(map(lambda x: x[::-1], words))

# 67. Map ile sayıların faktöriyelini hesaplama
import math
nums = [3, 4, 5]
factorials = list(map(math.factorial, nums))

# 68. Map ile kelimelerin ilk harflerini alma
words = ["apple", "banana", "cherry"]
first_letters = list(map(lambda x: x[0], words))

# 69. Map ile listedeki sayıları belirli bir aralıkta normalize etme
numbers = [10, 20, 30, 40]
normalized = list(map(lambda x: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers))

# 70. Map ve zip kullanarak iki listeyi dictionary'ye çevirme
keys = ["name", "age", "city"]
values = ["Ali", 25, "Istanbul"]
info_dict = dict(map(lambda k, v: (k, v), keys, values))
# 71. Lambda ile üs alma fonksiyonu
power = lambda x, y: x ** y

# 72. Lambda ile pozitif-negatif kontrolü
check_sign = lambda x: "Pozitif" if x > 0 else "Negatif"

# 73. Lambda ve filter ile negatif sayıları filtreleme
numbers = [-10, -5, 0, 5, 10]
positives = list(filter(lambda x: x > 0, numbers))

# 74. Lambda ile bir sayının mutlak değerini hesaplama
absolute = lambda x: x if x >= 0 else -x

# 75. Lambda ile liste elemanlarını tersine çevirme
reverse_list = lambda lst: lst[::-1]
# 76. Dictionary comprehension ile listeden dictionary oluşturma
names = ["Ali", "Ayşe", "Mehmet"]
ages = [25, 22, 30]
people_dict = {name: age for name, age in zip(names, ages)}

# 77. İç içe list comprehension ile çarpım tablosu oluşturma
multiplication_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]

# 78. Lambda, map ve dictionary ile isimlerin baş harflerini alma
names = ["Ali", "Ayşe", "Mehmet"]
initials_dict = {name: list(map(lambda x: x[0], name.split()))[0] for name in names}

# 79. List comprehension ve tuple kullanarak öğrenci notları
students = [("Ali", 85), ("Ayşe", 90), ("Mehmet", 75)]
high_achievers = [name for name, grade in students if grade > 80]

# 80. List comprehension ile iki listenin çarpımını alma
list1 = [1, 2, 3]
list2 = [4, 5, 6]
product_list = [a * b for a, b in zip(list1, list2)]

# 81. Dictionary içindeki sayısal değerleri filtreleme
data = {"a": 10, "b": "hello", "c": 20}
numeric_data = {k: v for k, v in data.items() if isinstance(v, int)}

# 82. Map ve filter kullanarak sadece çift sayıların karelerini alma
numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# 83. Lambda, map ve reduce kullanarak toplam bulma
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)

# 84. Tuple ve dictionary kullanarak şehirlerin nüfusunu listeleme
cities = (("Istanbul", 15000000), ("Ankara", 5500000), ("Izmir", 4300000))
city_population = {city: population for city, population in cities}

# 85. List comprehension ve lambda ile çift sayıları işaretleme
numbers = [1, 2, 3, 4, 5]
marked_numbers = [("Çift" if x % 2 == 0 else "Tek") for x in numbers]
# 86. Liste içindeki kelimeleri ters çevirme
words = ["python", "data", "science"]
reversed_words = [word[::-1] for word in words]

# 87. Liste içindeki kelimeleri uzunluklarına göre filtreleme (3 harften uzun olanlar)
long_words = [word for word in words if len(word) > 3]

# 88. ASCII kodları belirli bir aralıkta olan karakterleri listeleme
ascii_chars = [chr(i) for i in range(65, 91)]  # Büyük harfler (A-Z)

# 89. Çift sayıları listeye ekleyip, tekleri "Tek" olarak işaretleme
number_list = [x if x % 2 == 0 else "Tek" for x in range(10)]

# 90. Bir listenin içindeki en büyük sayıyı çıkartarak yeni liste oluşturma
numbers = [10, 50, 20, 40, 30]
filtered_numbers = [x for x in numbers if x != max(numbers)]
# 91. Tuple içinde en uzun string'i bulma
words_tuple = ("hello", "world", "python")
longest_word = max(words_tuple, key=len)

# 92. Tuple içindeki sayıların ortalamasını alma
numbers_tuple = (10, 20, 30, 40, 50)
average = sum(numbers_tuple) / len(numbers_tuple)

# 93. İç içe tuple kullanarak öğrenci bilgilerini sıralama
students = (("Ali", 85), ("Ayşe", 90), ("Mehmet", 75))
sorted_students = tuple(sorted(students, key=lambda x: x[1], reverse=True))

# 94. Tuple içindeki elemanları belirli bir formatta yazdırma
formatted_output = ", ".join(str(x) for x in numbers_tuple)

# 95. Tuple içindeki pozitif ve negatif sayıları ayırma
numbers_tuple = (-10, 20, -30, 40, -50)
positives = tuple(x for x in numbers_tuple if x > 0)
negatives = tuple(x for x in numbers_tuple if x < 0)
# 96. Dictionary içindeki en büyük değeri olan anahtarı bulma
scores = {"Ali": 85, "Ayşe": 90, "Mehmet": 75}
max_key = max(scores, key=scores.get)

# 97. Dictionary içindeki string değerleri ters çevirme
data = {"name": "Ali", "city": "Istanbul"}
reversed_data = {k: v[::-1] for k, v in data.items()}

# 98. Dictionary içindeki sayısal değerleri iki katına çıkarma
nums_dict = {"a": 2, "b": 3, "c": 4}
doubled_dict = {k: v * 2 for k, v in nums_dict.items()}

# 99. Dictionary'de yalnızca belirli uzunluktaki string'leri filtreleme
words_dict = {"a": "hello", "b": "hi", "c": "world"}
filtered_dict = {k: v for k, v in words_dict.items() if len(v) > 2}

# 100. Dictionary'yi ters çevirme (anahtarları ve değerleri yer değiştirme)
flipped_dict = {v: k for k, v in scores.items()}
# 101. Liste içindeki sayıları 2 ile çarpma
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

# 102. Liste içindeki sayıları string formatına çevirme
num_strings = list(map(str, numbers))

# 103. Map ve lambda ile negatif sayıları pozitif yapma
negative_numbers = [-5, -10, -15]
positives = list(map(lambda x: abs(x), negative_numbers))

# 104. İki listenin elemanlarını toplayarak yeni liste oluşturma
a = [1, 2, 3]
b = [4, 5, 6]
summed_list = list(map(lambda x, y: x + y, a, b))

# 105. Map ve lambda ile string'lerin baş harflerini alma
words = ["Ali", "Ayşe", "Mehmet"]
initials = list(map(lambda x: x[0], words))
# 106. Lambda ile asal sayı kontrolü
is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False

# 107. Lambda ile string uzunluğu hesaplama
length = lambda s: len(s)

# 108. Lambda ile yılın artık yıl olup olmadığını kontrol etme
is_leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 109. Lambda ve filter ile sadece pozitif sayıları alma
numbers = [-10, -5, 0, 5, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))

# 110. Lambda ile liste içindeki en büyük elemanı bulma
max_number = lambda lst: max(lst)
# 111. List comprehension ve dictionary comprehension ile liste içindeki kelimelerin uzunluklarını alma
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}

# 112. Map ve lambda ile bir listenin elemanlarını karesini alıp dictionary'ye çevirme
numbers = [1, 2, 3, 4, 5]
squared_dict = dict(map(lambda x: (x, x**2), numbers))

# 113. Lambda, filter ve map kullanarak liste içindeki çift sayıların karelerini alma
numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# 114. Dictionary comprehension ile liste içindeki sayıları tek veya çift olarak işaretleme
numbers = [1, 2, 3, 4, 5]
parity_dict = {x: "Çift" if x % 2 == 0 else "Tek" for x in numbers}

# 115. Map ve lambda kullanarak tarih formatını değiştirme
dates = ["2025-03-11", "2024-06-20", "2023-09-15"]
formatted_dates = list(map(lambda x: "/".join(x.split("-")[::-1]), dates))
# 116. Çift sayıları '*' ile değiştirme
numbers = [1, 2, 3, 4, 5, 6]
modified_list = [x if x % 2 != 0 else '*' for x in numbers]

# 117. String listesinde kelimeleri büyük harfe çevirme
words = ["python", "data", "science"]
uppercase_words = [word.upper() for word in words]

# 118. Listede yalnızca rakamlardan oluşan string'leri alma
mixed_list = ["123", "abc", "456", "def"]
digit_strings = [x for x in mixed_list if x.isdigit()]

# 119. Pozitif ve negatif sayıları ayrı listelere ayırma
numbers = [-5, 10, -15, 20, -25, 30]
positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]

# 120. İç içe list comprehension ile 3x3 birim matris oluşturma
identity_matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
# 121. Tuple içindeki sayıları string formatına çevirme
numbers_tuple = (10, 20, 30)
string_tuple = tuple(map(str, numbers_tuple))

# 122. Tuple içindeki en küçük elemanı bulma
min_value = min(numbers_tuple)

# 123. Tuple içindeki string'lerin uzunluklarını listeye çevirme
words_tuple = ("apple", "banana", "cherry")
lengths_list = [len(word) for word in words_tuple]

# 124. Tuple içindeki sayıların toplamını hesaplama
total_sum = sum(numbers_tuple)

# 125. Tuple içindeki kelimeleri alfabetik olarak sıralama
sorted_words = tuple(sorted(words_tuple))
# 126. Dictionary anahtarlarını büyük harf yapma
data = {"name": "Ali", "city": "Istanbul"}
upper_keys_dict = {k.upper(): v for k, v in data.items()}

# 127. Dictionary içindeki değerleri string formatına çevirme
mixed_dict = {"a": 10, "b": "hello", "c": 20}
string_dict = {k: str(v) for k, v in mixed_dict.items()}

# 128. Dictionary içindeki sayısal değerleri 3 ile çarpma
multiplied_dict = {k: v * 3 for k, v in mixed_dict.items() if isinstance(v, int)}

# 129. Dictionary anahtarlarını alfabetik sıralama
sorted_dict = {k: mixed_dict[k] for k in sorted(mixed_dict)}

# 130. Dictionary içindeki değerleri tersine çevirme (string olanları)
reversed_values_dict = {k: v[::-1] if isinstance(v, str) else v for k, v in mixed_dict.items()}
# 131. Map ile kelimelerin ilk iki harfini alma
words = ["apple", "banana", "cherry"]
first_two_chars = list(map(lambda x: x[:2], words))

# 132. Map ile liste içindeki sayıları string formatına çevirme
numbers = [10, 20, 30]
string_numbers = list(map(str, numbers))

# 133. Map ile liste içindeki string'leri ters çevirme
reversed_words = list(map(lambda x: x[::-1], words))

# 134. Map ve lambda ile kelimelerin uzunluklarını listeye alma
word_lengths = list(map(lambda x: len(x), words))

# 135. Map ve lambda ile listedeki çift sayıları iki katına çıkarma
numbers = [1, 2, 3, 4, 5, 6]
doubled_evens = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
# 136. Lambda ile üç sayı arasından en büyüğünü bulma
max_of_three = lambda a, b, c: max(a, b, c)

# 137. Lambda ile string içinde belirli bir harf olup olmadığını kontrol etme
contains_char = lambda s, char: char in s

# 138. Lambda ile girilen string’in palindrome olup olmadığını kontrol etme
is_palindrome = lambda s: s == s[::-1]

# 139. Lambda ile kelimenin tersini döndürme
reverse_string = lambda s: s[::-1]

# 140. Lambda ile metin içindeki kelimeleri büyük harfe çevirme
uppercase_words = lambda text: " ".join(word.upper() for word in text.split())
# 141. Dictionary comprehension ile sayıların faktöriyelini hesaplama
import math
numbers = [1, 2, 3, 4, 5]
factorial_dict = {num: math.factorial(num) for num in numbers}

# 142. List comprehension ve dictionary comprehension ile tersine çevirme
data = {"Ali": 85, "Ayşe": 90, "Mehmet": 75}
flipped_dict = {v: k for k, v in data.items()}

# 143. İç içe map ve lambda kullanarak liste içindeki string’leri ters çevirme
words = ["hello", "world"]
reversed_words = list(map(lambda x: "".join(map(lambda y: y, reversed(x))), words))

# 144. Filter ve lambda ile listeden yalnızca harf içeren elemanları filtreleme
mixed_list = ["123", "abc", "456", "def"]
only_strings = list(filter(lambda x: x.isalpha(), mixed_list))

# 145. Tuple içindeki elemanları listeye çevirip, tek olanları filtreleme
numbers_tuple = (1, 2, 3, 4, 5)
odd_numbers = [x for x in numbers_tuple if x % 2 != 0]

# 146. Map, filter ve lambda kullanarak string listesinde 5 harften uzun olanları ters çevirme
words = ["apple", "banana", "cherry", "fig", "grape"]
long_reversed_words = list(map(lambda x: x[::-1], filter(lambda x: len(x) > 5, words)))

# 147. Dictionary içindeki değerleri listeye çevirme ve toplamlarını hesaplama
data = {"A": [1, 2, 3], "B": [4, 5, 6]}
sum_values = {k: sum(v) for k, v in data.items()}

# 148. İç içe list comprehension ile satır satır matris oluşturma
matrix = [[i + j for j in range(5)] for i in range(5)]

# 149. Dictionary comprehension ile her harfin ASCII kodunu bulma
ascii_dict = {chr(i): i for i in range(65, 91)}

# 150. İç içe lambda kullanarak çift sayıları filtreleme ve karesini alma
numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
#for örnekler
"""
