FROM ubuntu:16.04

RUN useradd eg_classificator

WORKDIR /home/eg_classificator

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
libsm6 libxrender1 libfontconfig1 libice6 \
libglib2.0-0 libxext6 libgl1-mesa-glx

RUN apt-get install -y python3
RUN apt-get install -y python3-venv
RUN python3 -m venv venv
RUN venv/bin/pip3 install --upgrade pip
# RUN venv/bin/pip3 install --upgrade setuptools
RUN venv/bin/pip3 install -r requirements.txt

COPY app app
COPY eg_classificator.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP eg_classificator.py

RUN chown -R eg_classificator:eg_classificator ./
USER eg_classificator

EXPOSE 8000
CMD ["/bin/bash", "./boot.sh"]
