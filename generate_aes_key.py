import os

# Создаем случайный 32-байтовый ключ
aes_key = os.urandom(32)

# Сохраняем его в файл
with open("aes.key", "wb") as f:
    f.write(aes_key)

print("🔑 AES-ключ создан!")

