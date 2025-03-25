from Crypto.PublicKey import RSA

# Генерируем 2048-битные ключи
key = RSA.generate(2048)

# Сохраняем закрытый ключ
with open("private.pem", "wb") as f:
    f.write(key.export_key())

# Сохраняем открытый ключ
with open("public.pem", "wb") as f:
    f.write(key.publickey().export_key())

print("🔑 Ключи созданы!")

