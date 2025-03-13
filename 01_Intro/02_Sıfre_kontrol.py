"""try:
    sifre = input("Şifrenizi girin: ")

    if len(sifre) >= 16 and \
    any(c.isupper() for c in sifre) and \
    any(c.islower() for c in sifre) and \
    any(c.isdigit() for c in sifre) and \
    any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in sifre) and \
    not any(c == '-' for c in sifre):
        print("Şifre geçerli!")
    else:
        print("Şifre geçersiz. Lütfen kurallara uygun bir şifre girin.")

except Exception as hata:
    print(f"Bir hata oluştu: {hata}")"""


try:
    sifre = input("Şifrenizi girin: ")

    if len(sifre) >= 16 and \
    any(c.isupper() for c in sifre) and \
    any(c.islower() for c in sifre) and \
    any(c.isdigit() for c in sifre) and \
    any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in sifre):
        print("Şifre geçerli!")
    else:
        print("Şifre geçersiz. Lütfen kurallara uygun bir şifre girin.")

except Exception as hata:
    print(f"Bir hata oluştu: {hata}")

try:
    sifre = input("Şifrenizi girin: ")

    if len(sifre) >= 16 and \
    any(c.isupper() for c in sifre) and \
    any(c.islower() for c in sifre) and \
    any(c.isdigit() for c in sifre) and \
    any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in sifre) and \
    not any(c == '-' for c in sifre):
        print("Şifre geçerli!")
    else:
        print("Şifre geçersiz. Lütfen kurallara uygun bir şifre girin.")

except Exception as hata:
    print(f"Bir hata oluştu: {hata}")

