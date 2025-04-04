import sys
import json
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox,
    QComboBox, QCheckBox, QSpinBox
)

# Kullanıcı verilerini yükle
with open("kullanicilar.json", "r") as dosya:
    kullanicilar = json.load(dosya)

# Uçuş verileri
rotalar = [
    ("İstanbul", "Ankara"), ("Ankara", "İstanbul"),
    ("İstanbul", "İzmir"), ("İzmir", "İstanbul"),
    ("İstanbul", "Antalya"), ("Antalya", "İstanbul")
]

baslangic_saati = datetime.datetime.strptime("06:00", "%H:%M")
bitis_saati = datetime.datetime.strptime("23:30", "%H:%M")
aralik = datetime.timedelta(minutes=30)

temp_time = baslangic_saati
ucuslar = {}
while temp_time <= bitis_saati:
    for rota in rotalar:
        ucuslar[(rota[0], rota[1], temp_time.strftime("%H:%M"))] = {
            "yolcular": [], "koltuklar": list(range(1, 13))
        }
    temp_time += aralik

class LoginEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uçuş Rezervasyon Sistemi - Giriş")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.kullanici_adi_label = QLabel("Kullanıcı Adı:")
        self.kullanici_adi_input = QLineEdit()
        self.layout.addWidget(self.kullanici_adi_label)
        self.layout.addWidget(self.kullanici_adi_input)

        self.sifre_label = QLabel("Şifre:")
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.sifre_label)
        self.layout.addWidget(self.sifre_input)

        self.giris_butonu = QPushButton("Giriş Yap")
        self.giris_butonu.clicked.connect(self.giris_kontrol)
        self.layout.addWidget(self.giris_butonu)

        self.setLayout(self.layout)

    def giris_kontrol(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()

        if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:
            QMessageBox.information(self, "Başarılı Giriş", "Giriş başarılı!")
            self.hide()
            self.rezervasyon_ekrani = RezervasyonEkrani(kullanici_adi)
            self.rezervasyon_ekrani.show()
        else:
            QMessageBox.warning(self, "Hatalı Giriş", "Kullanıcı adı veya şifre hatalı!")

class RezervasyonEkrani(QWidget):
    def __init__(self, kullanici_adi):
        super().__init__()
        self.setWindowTitle("Rezervasyon Ekranı")
        self.setGeometry(100, 100, 400, 400)
        self.kullanici = kullanici_adi

        self.layout = QVBoxLayout()

        self.label = QLabel(f"Hoş geldiniz, {kullanici_adi}!")
        self.layout.addWidget(self.label)

        # Kalkış ve varış seçimi
        self.kalkis_combo = QComboBox()
        self.varis_combo = QComboBox()
        sehirler = sorted(set([sehir for rota in rotalar for sehir in rota]))
        self.kalkis_combo.addItems(sehirler)
        self.varis_combo.addItems(sehirler)
        self.layout.addWidget(QLabel("Kalkış Şehri:"))
        self.layout.addWidget(self.kalkis_combo)
        self.layout.addWidget(QLabel("Varış Şehri:"))
        self.layout.addWidget(self.varis_combo)

        # Saat seçimi
        self.saat_combo = QComboBox()
        temp = baslangic_saati
        while temp <= bitis_saati:
            self.saat_combo.addItem(temp.strftime("%H:%M"))
            temp += aralik
        self.layout.addWidget(QLabel("Saat Seçimi:"))
        self.layout.addWidget(self.saat_combo)

        # Diğer bilgiler
        self.bilet_turu_combo = QComboBox()
        self.bilet_turu_combo.addItems(["ekonomi", "business"])
        self.yolcu_turu_combo = QComboBox()
        self.yolcu_turu_combo.addItems(["yetişkin", "çocuk"])
        self.gidis_donus_check = QCheckBox("Gidiş-Dönüş")
        self.otel_check = QCheckBox("Otel Ekle")
        self.layout.addWidget(QLabel("Bilet Türü:"))
        self.layout.addWidget(self.bilet_turu_combo)
        self.layout.addWidget(QLabel("Yolcu Türü:"))
        self.layout.addWidget(self.yolcu_turu_combo)
        self.layout.addWidget(self.gidis_donus_check)
        self.layout.addWidget(self.otel_check)

        # Koltuk seçimi
        self.koltuk_secim = QSpinBox()
        self.koltuk_secim.setRange(1, 12)
        self.layout.addWidget(QLabel("Koltuk Numarası:"))
        self.layout.addWidget(self.koltuk_secim)

        self.rezervasyon_btn = QPushButton("Rezervasyon Yap")
        self.rezervasyon_btn.clicked.connect(self.rezervasyon_yap)
        self.layout.addWidget(self.rezervasyon_btn)

        self.setLayout(self.layout)

    def rezervasyon_yap(self):
        kalkis = self.kalkis_combo.currentText()
        varis = self.varis_combo.currentText()
        saat = self.saat_combo.currentText()
        bilet_turu = self.bilet_turu_combo.currentText()
        yolcu_turu = self.yolcu_turu_combo.currentText()
        gidis_donus = self.gidis_donus_check.isChecked()
        otel = self.otel_check.isChecked()
        koltuk = self.koltuk_secim.value()

        anahtar = (kalkis, varis, saat)
        if kalkis == varis:
            QMessageBox.warning(self, "Hatalı Seçim", "Kalkış ve varış şehirleri aynı olamaz!")
            return

        if anahtar not in ucuslar:
            QMessageBox.warning(self, "Hata", "Uçuş bulunamadı!")
            return

        if koltuk in ucuslar[anahtar]["yolcular"]:
            QMessageBox.warning(self, "Dolu Koltuk", "Bu koltuk dolu. Başka bir koltuk seçin.")
            return

        ucuslar[anahtar]["yolcular"].append(koltuk)

        # Fiyat hesaplama
        saat_dilim = int(saat.split(":")[0])
        if 6 <= saat_dilim < 12:
            fiyat = {"ekonomi": 4600, "business": 8900}[bilet_turu]
        elif 12 <= saat_dilim < 18:
            fiyat = {"ekonomi": 5500, "business": 9800}[bilet_turu]
        else:
            fiyat = {"ekonomi": 6300, "business": 11000}[bilet_turu]

        if yolcu_turu == "çocuk":
            fiyat -= 3000
            fiyat = max(fiyat, 0)
        if gidis_donus:
            fiyat = fiyat * 2 * 0.9
        if otel:
            fiyat += 4000

        QMessageBox.information(self, "Rezervasyon Tamamlandı",
            f"Rezervasyon başarılı!\nKoltuk: {koltuk}\nToplam Ücret: {fiyat} TL")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = LoginEkrani()
    pencere.show()
    sys.exit(app.exec_())
