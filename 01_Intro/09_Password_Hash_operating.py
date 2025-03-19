"""import bcrypt

# Şifreyi hashlemek
def hash_sifre(sifre):
    salt = bcrypt.gensalt()  # Rastgele salt üretir
    hashed = bcrypt.hashpw(sifre.encode(), salt)  # Şifreyi hashler
    return hashed

# Şifreyi doğrulamak
def sifre_dogrula(sifre, hashed_sifre):
    return bcrypt.checkpw(sifre.encode(), hashed_sifre)

# Örnek kullanım
sifre = "gizli123"
hashed_sifre = hash_sifre(sifre)
print(f"Hashlenmiş Şifre: {hashed_sifre}")

# Doğrulama
print(sifre_dogrula("gizli123", hashed_sifre))  # True
print(sifre_dogrula("yanlisSifre", hashed_sifre))  # False"""


import bcrypt
import bcrypt
import string

# Kullanıcıları saklayacağımız liste
users = []


def hash_password(password: str) -> str:
    """Şifreyi bcrypt ile hashler."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()  # Byte formatını stringe çeviriyoruz


def is_pwd_valid(password: str) -> bool:
    """Şifrenin geçerli olup olmadığını kontrol eder."""
    char_set = set(password)

    return (
            len(password) >= 16 and
            any(c in string.ascii_uppercase for c in char_set) and  # En az bir büyük harf
            any(c in string.ascii_lowercase for c in char_set) and  # En az bir küçük harf
            any(c in string.digits for c in char_set) and  # En az bir rakam
            any(c in string.punctuation for c in char_set)  # En az bir özel karakter
    )


def sign_up(username: str, password: str) -> str:
    """Yeni kullanıcı kaydı yapar."""
    # Kullanıcı adının var olup olmadığını kontrol et
    is_username_exist = any(user[0] == username for user in users)

    if is_username_exist:
        return 'Bu kullanıcı adı zaten alınmış.'

    if not is_pwd_valid(password):
        return 'Geçersiz şifre! Şifre en az 16 karakter olmalı ve büyük/küçük harf, rakam, özel karakter içermelidir.'

    # Şifreyi hashle ve kaydet
    hashed_password = hash_password(password)
    users.append((username, hashed_password))

    return 'Üyelik işlemi tamamlandı!'


# Örnek kullanım
#print(sign_up("test_user", "GüçlüSifre123!@#"))  # Başarılı kayıt
#print(sign_up("test_user", "ZayıfŞifre"))  # Geçersiz şifre
#print(sign_up("test_user", "GüçlüSifre123!@#"))  # Kullanıcı adı zaten alınmış




