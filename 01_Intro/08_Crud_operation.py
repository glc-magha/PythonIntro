# 1. Listeyi oluşturma (Create)
data = []

# 2. Veriyi ekleme (Create)
data.append("Veri 1")

# 3. Veriyi okuma (Read)
print(data[0])

# 4. Veriyi güncelleme (Update)
data[0] = "Güncellenmiş Veri 1"

# 5. Veriyi silme (Delete)
del data[0]

# 6. Veriyi ekleme
data.append("Veri 2")

# 7. Veriyi ekleme
data.append("Veri 3")

# 8. Listeyi okuma
print(data)

# 9. Belirli bir veri arama (Read)
print("Veri 2" in data)

# 10. Veri ekleme (Create)
data.append("Veri 4")

# 11. Veriyi güncelleme (Update)
data[2] = "Güncellenmiş Veri 3"

# 12. Veri silme (Delete)
data.remove("Veri 4")

# 13. Veriyi ekleme
data.append("Veri 5")

# 14. Veriyi okuma
print(data)

# 15. Listeyi sıralama (Read)
data.sort()

# 16. Veriyi ekleme
data.append("Veri 6")

# 17. Veriyi güncelleme
data[4] = "Güncellenmiş Veri 5"

# 18. Veri silme
data.pop()

# 19. Veri ekleme
data.append("Veri 7")

# 20. Veriyi okuma
print(data)

# 21. Listeyi tersine çevirme (Read)
data.reverse()

# 22. Veri ekleme
data.append("Veri 8")

# 23. Veri güncelleme
data[1] = "Güncellenmiş Veri 2"

# 24. Veri silme
del data[3]

# 25. Veri ekleme
data.append("Veri 9")

# 26. Veriyi okuma
print(data)

# 27. Listeyi sıralama
data.sort()

# 28. Veri ekleme
data.append("Veri 10")

# 29. Veriyi güncelleme
data[0] = "Güncellenmiş Veri 10"

# 30. Veri silme
data.pop(2)

# 31. Veri ekleme
data.append("Veri 11")

# 32. Veriyi okuma
print(data)

# 33. Listeyi tersine çevirme
data.reverse()

# 34. Veri güncelleme
data[1] = "Güncellenmiş Veri 11"

# 35. Veri silme
data.remove("Veri 9")

# 36. Veri ekleme
data.append("Veri 12")

# 37. Veriyi okuma
print(data)

# 38. Listeyi sıralama
data.sort()

# 39. Veri ekleme
data.append("Veri 13")

# 40. Veriyi güncelleme
data[3] = "Güncellenmiş Veri 12"

# 41. Veri silme
data.pop(1)

# 42. Veri ekleme
data.append("Veri 14")

# 43. Veriyi okuma
print(data)

# 44. Listeyi tersine çevirme
data.reverse()

# 45. Veri güncelleme
data[2] = "Güncellenmiş Veri 13"

# 46. Veri silme
del data[4]

# 47. Veri ekleme
data.append("Veri 15")

# 48. Veriyi okuma
print(data)

# 49. Listeyi sıralama
data.sort()

# 50. Veri silme
data.clear()

# Sonuçları kontrol etme
print(data)


#BASİT CRUD SINIF YAPISI
class DataManager:
    def __init__(self):
        self.data = []

    def create(self, item):
        self.data.append(item)

    def read(self):
        return self.data

    def update(self, index, new_item):
        if 0 <= index < len(self.data):
            self.data[index] = new_item
        else:
            print("Index hatalı!")

    def delete(self, item):
        if item in self.data:
            self.data.remove(item)
        else:
            print("Veri bulunamadı.")


# Kullanım
manager = DataManager()
manager.create("Veri 1")
manager.create("Veri 2")
print(manager.read())
manager.update(1, "Güncellenmiş Veri 2")
manager.delete("Veri 1")
print(manager.read())

#Sözlük Kullanarak CRUD İşlemleri
class DictionaryManager:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        self.data[key] = value

    def read(self, key):
        return self.data.get(key, "Key bulunamadı.")

    def update(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
        else:
            print("Key bulunamadı!")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print("Key bulunamadı!")


# Kullanım
dict_manager = DictionaryManager()
dict_manager.create("id1", "Veri 1")
dict_manager.create("id2", "Veri 2")
print(dict_manager.read("id1"))
dict_manager.update("id1", "Güncellenmiş Veri 1")
dict_manager.delete("id2")
print(dict_manager.read("id2"))
#Dosya İle CRUD İşlemleri
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def create(self, content):
        with open(self.filename, 'a') as file:
            file.write(content + '\n')

    def read(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def update(self, old_content, new_content):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        with open(self.filename, 'w') as file:
            for line in lines:
                file.write(line.replace(old_content, new_content))

    def delete(self, content):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        with open(self.filename, 'w') as file:
            for line in lines:
                if content not in line:
                    file.write(line)


# Kullanım
file_manager = FileManager('data.txt')
file_manager.create('Veri 1')
file_manager.create('Veri 2')
print(file_manager.read())
file_manager.update('Veri 1', 'Güncellenmiş Veri 1')
file_manager.delete('Veri 2')
print(file_manager.read())
#JSON Veri Yapısı Kullanarak CRUD İşlemleri
import json

class JsonManager:
    def __init__(self, filename):
        self.filename = filename

    def create(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def read(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def update(self, key, new_value):
        data = self.read()
        if key in data:
            data[key] = new_value
            self.create(data)
        else:
            print("Key bulunamadı.")

    def delete(self, key):
        data = self.read()
        if key in data:
            del data[key]
            self.create(data)
        else:
            print("Key bulunamadı.")

# Kullanım
json_manager = JsonManager('data.json')
json_manager.create({"id1": "Veri 1", "id2": "Veri 2"})
print(json_manager.read())
json_manager.update("id1", "Güncellenmiş Veri 1")
json_manager.delete("id2")
print(json_manager.read())
#Veritabanı Bağlantısı ile CRUD (SQLite)
import sqlite3


class SqliteManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)''')

    def create(self, value):
        self.cursor.execute("INSERT INTO data (value) VALUES (?)", (value,))
        self.conn.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()

    def update(self, id, new_value):
        self.cursor.execute("UPDATE data SET value = ? WHERE id = ?", (new_value, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM data WHERE id = ?", (id,))
        self.conn.commit()


# Kullanım
sqlite_manager = SqliteManager('data.db')
sqlite_manager.create("Veri 1")
sqlite_manager.create("Veri 2")
print(sqlite_manager.read())
sqlite_manager.update(1, "Güncellenmiş Veri 1")
sqlite_manager.delete(2)
print(sqlite_manager.read())
#Linked List Kullanarak CRUD İşlemleri
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def read(self):
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print("Veri bulunamadı.")

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print("Veri bulunamadı.")


# Kullanım
linked_list = LinkedList()
linked_list.create("Veri 1")
linked_list.create("Veri 2")
linked_list.create("Veri 3")
print(linked_list.read())
linked_list.update("Veri 2", "Güncellenmiş Veri 2")
linked_list.delete("Veri 1")
print(linked_list.read())
#Pandas Kullanarak CRUD İşlemleri (Veri Çerçevesi)
import pandas as pd


class PandasManager:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.DataFrame(columns=["id", "value"])

    def create(self, id, value):
        self.df = self.df.append({"id": id, "value": value}, ignore_index=True)
        self.df.to_csv(self.filename, index=False)

    def read(self):
        return pd.read_csv(self.filename)

    def update(self, id, new_value):
        self.df.loc[self.df['id'] == id, 'value'] = new_value
        self.df.to_csv(self.filename, index=False)

    def delete(self, id):
        self.df = self.df[self.df['id'] != id]
        self.df.to_csv(self.filename, index=False)


# Kullanım
pandas_manager = PandasManager('data.csv')
pandas_manager.create(1, "Veri 1")
pandas_manager.create(2, "Veri 2")
print(pandas_manager.read())
pandas_manager.update(1, "Güncellenmiş Veri 1")
pandas_manager.delete(2)
print(pandas_manager.read())
#Queue (Kuyruk) Kullanarak CRUD İşlemleri
from collections import deque


class QueueManager:
    def __init__(self):
        self.queue = deque()

    def create(self, item):
        self.queue.append(item)

    def read(self):
        return list(self.queue)

    def update(self, old_item, new_item):
        if old_item in self.queue:
            index = self.queue.index(old_item)
            self.queue[index] = new_item
        else:
            print("Öğe bulunamadı.")

    def delete(self, item):
        if item in self.queue:
            self.queue.remove(item)
        else:
            print("Öğe bulunamadı.")


# Kullanım
queue_manager = QueueManager()
queue_manager.create("Veri 1")
queue_manager.create("Veri 2")
print(queue_manager.read())
queue_manager.update("Veri 1", "Güncellenmiş Veri 1")
queue_manager.delete("Veri 2")
print(queue_manager.read())
#Liste Kullanarak CRUD İşlemleri
# Basit bir liste ile CRUD işlemleri

# Create: Listeye veri eklemek
data = []
data.append("Veri 1")
data.append("Veri 2")
print("Listeye eklenen veriler:", data)

# Read: Listeyi okumak
print("Listeyi oku:", data)

# Update: Liste elemanını güncellemek
data[0] = "Güncellenmiş Veri 1"
print("Güncellenmiş liste:", data)

# Delete: Liste elemanını silmek
data.remove("Veri 2")
print("Silinen veri sonrası liste:", data)
#Sözlük Kullanarak CRUD İşlemleri# Basit bir sözlük ile CRUD işlemleri

# Create: Sözlüğe veri eklemek
data_dict = {}
data_dict["id1"] = "Veri 1"
data_dict["id2"] = "Veri 2"
print("Sözlüğe eklenen veriler:", data_dict)

# Read: Sözlüğü okumak
print("id1 verisi:", data_dict["id1"])

# Update: Sözlük elemanını güncellemek
data_dict["id1"] = "Güncellenmiş Veri 1"
print("Güncellenmiş sözlük:", data_dict)

# Delete: Sözlük elemanını silmek
del data_dict["id2"]
print("Silinen veri sonrası sözlük:", data_dict)
#Kullanıcı Girişi ile CRUD İşlemleri
# Kullanıcıdan veri alarak CRUD işlemleri

data_list = []

# Create: Kullanıcıdan veri almak ve listeye eklemek
def add_data():
    new_data = input("Yeni veri girin: ")
    data_list.append(new_data)
    print("Veri eklendi:", data_list)

# Read: Listeyi görüntülemek
def view_data():
    print("Tüm veriler:", data_list)

# Update: Liste elemanını güncellemek
def update_data():
    index = int(input("Güncellemek istediğiniz veri numarasını girin (0, 1, 2, ...): "))
    if 0 <= index < len(data_list):
        new_value = input("Yeni değeri girin: ")
        data_list[index] = new_value
        print("Güncellenmiş liste:", data_list)
    else:
        print("Geçersiz index!")

# Delete: Liste elemanını silmek
def delete_data():
    value = input("Silmek istediğiniz veriyi girin: ")
    if value in data_list:
        data_list.remove(value)
        print("Veri silindi:", data_list)
    else:
        print("Veri bulunamadı.")

# Kullanıcı etkileşimi
add_data()
view_data()
update_data()
delete_data()




#Basit Sayılarla CRUD İşlemleri
# Basit bir sayı listesiyle CRUD işlemleri

numbers = [1, 2, 3, 4, 5]

# Create: Sayı eklemek
numbers.append(6)
print("Yeni sayı ekledik:", numbers)

# Read: Sayıları okumak
print("Tüm sayılar:", numbers)

# Update: Sayıyı değiştirmek
numbers[0] = 10
print("Güncellenmiş sayılar:", numbers)

# Delete: Sayıyı silmek
numbers.remove(3)
print("Silinen sayı sonrası:", numbers)



#Basit Bir Hesap Makinesi (CRUD Benzeri İşlemler)
# Basit bir hesap makinesi ile CRUD işlemleri
class Calculator:
    def __init__(self):
        self.result = 0

    # Create (işlem başlatma)
    def add(self, value):
        self.result += value
        print("Toplam:", self.result)

    # Read (değer okuma)
    def read(self):
        print("Sonuç:", self.result)

    # Update (sonucu değiştirme)
    def set_result(self, value):
        self.result = value
        print("Sonuç güncellendi:", self.result)

    # Delete (sonucu sıfırlama)
    def reset(self):
        self.result = 0
        print("Sonuç sıfırlandı.")

# Kullanım
calc = Calculator()
calc.add(5)  # Create
calc.read()   # Read
calc.set_result(100)  # Update
calc.reset()  # Delete
#Liste Üzerinde Basit CRUD İşlemleri
# Liste üzerinde basit CRUD işlemleri

items = ["Elma", "Armut", "Muz"]




# Create: Listeye yeni bir öğe eklemek
items.append("Kiraz")
print("Yeni öğe ekledik:", items)

# Read: Listeyi okumak
print("Listeyi okuduk:", items)

# Update: Liste elemanını değiştirmek
items[1] = "Portakal"
print("Güncellenmiş liste:", items)

# Delete: Liste elemanını silmek
items.remove("Muz")
print("Silinen öğe sonrası liste:", items)





# Sayı listesi ile CRUD işlemleri

numbers = [10, 20, 30]

# Create: Yeni sayı eklemek
numbers.append(40)
print("Yeni sayı ekledik:", numbers)

# Read: Listeyi okumak
print("Tüm sayılar:", numbers)

# Update: Sayıyı güncellemek
numbers[1] = 25
print("Güncellenmiş sayılar:", numbers)

# Delete: Sayıyı silmek
numbers.remove(30)
print("Silinen sayı sonrası:", numbers)





