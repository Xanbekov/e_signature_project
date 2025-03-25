from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Файл, который подписываем
FILE_TO_SIGN = "document.txt"

# Читаем файл
with open(FILE_TO_SIGN, "rb") as f:
    data = f.read()

# Создаем хеш файла
hash_obj = SHA256.new(data)

# Загружаем закрытый ключ
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Подписываем хеш
signature = pkcs1_15.new(private_key).sign(hash_obj)

# Сохраняем подпись в файл
with open("signature.sig", "wb") as f:
    f.write(signature)

print("✅ Файл подписан!")

