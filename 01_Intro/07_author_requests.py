"""import requests

# API URL ve API Anahtarı (API anahtarınızı buraya ekleyin)
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "YOUR_API_KEY"  # Kendi API anahtarınızı girin

# API'ye gönderilecek parametreler
params = {
    "country": "us",   # ABD haberleri
    "category": "business",  # İş dünyası haberleri
    "apiKey": API_KEY  # API Anahtarı
}

# API isteğini gönder
response = requests.get(API_URL, params=params)

# Yanıtı kontrol et
if response.status_code == 200:
    data = response.json()  # JSON formatına çevir

    # Eğer makaleler geldiyse
    if "articles" in data:
        for article in data["articles"]:
            author = article.get("author", "Bilinmiyor")  # Yazar bilgisi
            title = article.get("title", "Başlık bulunamadı")  # Haber başlığı
            content = article.get("content", "İçerik bulunamadı")  # İçerik bilgisi
            published_at = article.get("publishedAt", "Tarih belirtilmemiş")  # Yayınlanma tarihi

            # Sonuçları ekrana yazdır
            print(f"📝 Yazar: {author}")
            print(f"📢 Başlık: {title}")
            print(f"📖 İçerik: {content}")
            print(f"📅 Yayınlanma Tarihi: {published_at}")
            print("-" * 50)

else:
    print(f"❌ Hata! Veri çekilemedi. HTTP Kod: {response.status_code}")"""


"""import requests

# API URL ve API Anahtarı
API_URL = "https://www.allthingsdev.co/"
API_KEY = "a325aacb-99e6-4b62-80e8-8b9703bc2f6c"  # Buraya kendi API anahtarınızı girin

# API isteği için parametreler
params = {
    "category": "business",  # İş dünyası haberlerini alıyoruz
    "limit": 5  # 5 haber getir
}

# API anahtarını header olarak ekleyerek isteği gönder
headers = {
    "Metric-Converter-API.allthingsdev.co": API_KEY
}

# API'ye istek gönder
response = requests.get(API_URL, headers=headers, params=params)

# Yanıtı kontrol et
if response.status_code == 200:
    data = response.json()  # JSON formatına çevir

    # Gelen yanıtı yazdır (Yanıt yapısını görmek için)
    print(data)

    # Gelen haberleri ekrana yazdır
    for article in data:
        author = article.get("author", "Bilinmiyor")  # Eğer "author" yoksa "Bilinmiyor" yazsın
        title = article.get("title", "Başlık bulunamadı")  # Haber başlığı
        content = article.get("content", "İçerik bulunamadı")  # İçerik bilgisi
        published_at = article.get("published_at", "Tarih belirtilmemiş")  # Tarih bilgisi

        print(f"📝 Yazar: {author}")
        print(f"📢 Başlık: {title}")
        print(f"📖 İçerik: {content}")
        print(f"📅 Yayınlanma Tarihi: {published_at}")
        print("-" * 50)

else:
    print("❌ Hata! Veri çekilemedi. HTTP Kod:", response.status_code)
"""

"""import requests

# API URL ve API Anahtarı
API_URL = "https://api.allthingsdev.com/endpoint"  # Bu URL'yi API dokümantasyonundan öğrenebilirsiniz
API_KEY = "a325aacb-99e6-4b62-80e8-8b9703bc2f6c"  # Kendi API anahtarınızı buraya ekleyin

# API'ye istek için parametreler (gerekirse API dökümantasyonundan öğrenebilirsiniz)
params = {
    "param1": "value1",  # Parametrelerinizi buraya ekleyin
    "param2": "value2",
    "apiKey": API_KEY  # API anahtarınız
}

# API isteği gönder
response = requests.get(API_URL, params=params)

# Yanıtı kontrol et
if response.status_code == 200:
    data = response.json()  # JSON formatına çevir

    # API'den dönen veriyi yazdır
    print(data)
else:
    print("Hata! HTTP Kod:", response.status_code)"""



"""
    import requests

    name = 'platinum'
    api_url = 'https://api.api-ninjas.com/v1/commodityprice?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)"""

"""import requests

# API URL ve API Anahtarı
API_URL = "https://api.allthingsdev.com/endpoint"
API_KEY = "a325aacb-99e6-4b62-80e8-8b9703bc2f6c"  # Buraya kendi API anahtarınızı ekleyin

# Kullanıcıdan yazar adı al
author_name = input("Yazar adı girin: ")

# API'ye istek için parametreler
params = {
    "q": author_name,  # Kullanıcı tarafından girilen yazar adı ile arama yapıyoruz
    "apiKey": API_KEY,  # API anahtarı
    "language": "tr",  # Türkçe makaleler almak için (gerekirse dil parametresini değiştirebilirsiniz)
    "pageSize": 5  # Maksimum 5 makale al
}

# API isteği gönder
response = requests.get(API_URL, params=params)

# Yanıtı kontrol et
if response.status_code == 200:
    data = response.json()  # JSON formatına çevir

    # Eğer "articles" varsa, yani makaleler gelmişse
    if "articles" in data:
        articles = data["articles"]

        # Makaleleri ekrana yazdır
        if articles:
            for idx, article in enumerate(articles, start=1):
                title = article.get("title", "Başlık bulunamadı")
                description = article.get("description", "Açıklama bulunamadı")
                published_at = article.get("publishedAt", "Tarih belirtilmemiş")

                print(f"{idx}. Makale:")
                print(f"Başlık: {title}")
                print(f"Açıklama: {description}")
                print(f"Yayınlanma Tarihi: {published_at}")
                print("-" * 50)  # Ayraç
        else:
            print("Bu yazarla ilgili makale bulunamadı.")
    else:
        print("Makale verisi alınamadı.")
else:
    print(f"❌ Hata! HTTP Kod: {response.status_code}")
"""






