from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.exceptions import InvalidSignature
from base64 import b64decode
from Crypto.Cipher import AES
import os

# Загрузка публичного ключа для проверки подписи
def load_public_key():
    with open("public.pem", "rb") as f:
        return load_pem_public_key(f.read())

# Проверка ЭЦП
def verify_signature(file_path, signature_path, public_key):
    with open(file_path, "rb") as f:
        data = f.read()

    with open(signature_path, "rb") as sig_file:
        signature = sig_file.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("✅ Подпись файла верна!")
    except InvalidSignature:
        print("❌ Неверная подпись файла!")

# Расшифровка файла
def decrypt_file(file_path, key_path):
    with open(key_path, "rb") as f:
        key = f.read()

    # Расшифровка AES
    cipher = AES.new(key, AES.MODE_GCM)
    with open(file_path, "rb") as f:
        file_data = f.read()

    # Расшифровка данных
    decrypted_data = cipher.decrypt_and_verify(file_data, None)  # Для простоты не используем nonce и tag

    with open("decrypted_document.txt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("📂 Файл расшифрован и сохранён как decrypted_document.txt!")

# Основной процесс
if __name__ == "__main__":
    public_key = load_public_key()
    verify_signature("document.enc", "document.sig", public_key)  # Проверка подписи
    decrypt_file("document.enc", "aes.enc")  # Расшифровка файла

