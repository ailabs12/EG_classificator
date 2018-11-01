# EG_classificator 
REST-like API service for emotion and gender classification

# Run server
<<<<<<< HEAD
Чтобы запустить сервер на Flask локально, нужно прописать в консоли следующую вещь 
=======
для того, чтобы запустить сервер на Flask локально, нужно прописать в консоли следующую вещь 
>>>>>>> 552140b3668cdaec801e5ec9cc2e6a948daa96a6

export FLASK_APP=eg_classificator.py

Затем для запуска такого сервера используется команда 

flask run

ВАЖНО: для того, чтобы подтянуть все зависимости в проекте лежит файл requirements.txt. Чтобы не было конфликтов версий библиотек, необходимо создать виртуальное окружение. В python для этого можно использовать venv в python или virtualenvwrapper. https://python-scripts.com/virtualenv
Затем, чтобы установить необходимые зависимости нужно выполнить следующую команду в созданном виртуальном окружении

pip install -r requirements.txt

# Usage
https://emotionclassificatorapi10.docs.apiary.io
