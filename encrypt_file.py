from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

# Файл, который шифруем
FILE_TO_ENCRYPT = "document.txt"

# Читаем файл
with open(FILE_TO_ENCRYPT, "rb") as f:
    data = f.read()

# Загружаем AES-ключ
with open("aes.key", "rb") as f:
    aes_key = f.read()

# Шифруем файл AES-ключом
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# Сохраняем зашифрованный файл
with open("document.enc", "wb") as f:
    f.write(cipher_aes.nonce + tag + ciphertext)

# Загружаем открытый RSA-ключ
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Шифруем AES-ключ с помощью RSA
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

# Сохраняем зашифрованный AES-ключ
with open("aes.enc", "wb") as f:
    f.write(encrypted_aes_key)

print("🔒 Файл зашифрован и готов к отправке!")

