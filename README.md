# E-Signature Project

Этот проект реализует систему электронных подписей для файлов. Он включает в себя:

1. Генерацию публичных и приватных ключей RSA.
2. Подписание файла с использованием приватного ключа.
3. Шифрование файла с использованием AES.
4. Отправку зашифрованного файла по электронной почте.
5. Проверку подписи и расшифровку файла на стороне получателя.

## Структура проекта

- `generate_keys.py`: Генерация публичных и приватных ключей RSA.
- `sign_file.py`: Подписание файла с использованием приватного ключа.
- `encrypt_file.py`: Шифрование файла с использованием AES.
- `send_email.py`: Отправка зашифрованного файла по электронной почте.
- `receive_and_verify.py`: Расшифровка файла и проверка его подписи на стороне получателя.
- `document.txt`: Пример текстового документа для подписи и отправки.
- `requirements.txt`: Список зависимостей для проекта.

## Установка

###Клонируйте репозиторий###:
   ```bash
   git clone https://github.com/Xanbekov/e_signature_project.git

##Перейдите в папку с проектом:
cd e_signature_project

##Создайте и активируйте виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

##Установите необходимые зависимости:
pip install -r requirements.txt

##Использование##

##Генерация ключей RSA:
python generate_keys.py

##Подписание файла:
python sign_file.py document.txt

##Шифрование файла:
python encrypt_file.py document.txt

##Отправка зашифрованного файла:
python send_email.py

##Получение и проверка подписи:
python receive_and_verify.py
