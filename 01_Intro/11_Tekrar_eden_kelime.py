def tekrar_edeni_sil(cumle):
    kelimeler = cumle.split()  # Cümleyi boşluklardan ayırarak kelimeler listesi oluştur
    benzersiz_kelimeler = []  # Tekrar etmeyen kelimeleri saklamak için boş liste oluştur

    for kelime in kelimeler:  # Listedeki her kelimeyi kontrol et
        if kelime not in benzersiz_kelimeler:  # Eğer kelime listede yoksa ekle
            benzersiz_kelimeler.append(kelime)

    sonuc = " ".join(benzersiz_kelimeler)  # Benzersiz kelimeleri birleştirerek yeni bir cümle oluştur
    return sonuc


# Örnek kullanım
cumle = "merhaba ben burak burak ben merhaba"
print(tekrar_edeni_sil(cumle))



def alfabetik_sirala(cumle):
    kelimeler = cumle.split()  # Cümleyi kelimelere ayır
    kelimeler.sort()  # Kelimeleri alfabetik olarak sırala
    return " ".join(kelimeler)  # Tekrar birleştirerek döndür

# Örnek kullanım
cumle = input("Bir cümle girin: ")
print(alfabetik_sirala(cumle))

