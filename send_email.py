import smtplib
import ssl
from email.message import EmailMessage

# Данные для отправки
EMAIL_SENDER = "venum@gmail.com"  # Твой email
EMAIL_PASSWORD = "venum123"       # Пароль приложения
EMAIL_RECEIVER = "venum123@gmail.com"  # Кому отправляем

# Создаем письмо
msg = EmailMessage()
msg["Subject"] = "Зашифрованный файл"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Отправляю зашифрованный файл и ключ.")

# Прикрепляем файлы
for filename in ["document.enc", "aes.enc"]:
    with open(filename, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=filename)

# Отправка email с использованием TLS
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Запускаем защищённое соединение
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.send_message(msg)

print("📩 Файл отправлен!")


