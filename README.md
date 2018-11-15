# EG_classificator 
REST-like API service for emotion and gender classification

# Run server locally
Чтобы запустить сервер на Flask локально, нужно прописать в консоли следующую вещь 
```
export FLASK_APP=eg_classificator.py
```
Затем для запуска такого сервера используется команда 
```
flask run
```
ВАЖНО: для того, чтобы подтянуть все зависимости в проекте лежит файл requirements.txt. Чтобы не было конфликтов версий библиотек, необходимо создать виртуальное окружение. В python для этого можно использовать venv в python или virtualenvwrapper. https://python-scripts.com/virtualenv
Затем, чтобы установить необходимые зависимости нужно выполнить следующую команду в созданном виртуальном окружении
```
pip install -r requirements.txt
```
# Run server with Docker
Для того, чтобы запустить сервис с помощью Docker нужно сначала собрать Docker image:
```
cd eg_classificator
docker build -t eg_classificator:1.0 .
```
Затем чтобы запустить образ, нужно применить следующую команду:
```
docker run --name eg_classificator -d -p 8000:5000 --rm eg_calssificator:1.0
```
После запуска сервис будет доступен по адресу 0.0.0.0:8000

# Run server with Docker
Для того, чтобы запустить сервис с помощью Docker нужно сначала собрать Docker image:
```
cd eg_classificator
docker build -t eg_classificator:1.0 .
```
Затем чтобы запустить образ, нужно применить следующую команду:
```
docker run --name eg_classificator -d -p 8000:5000 --rm eg_calssificator:1.0
```
После запуска сервис будет доступен по адресу 0.0.0.0:8000

# Usage
https://emotionclassificatorapi10.docs.apiary.io
