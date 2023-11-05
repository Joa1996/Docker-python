FROM ubuntu:latest  


#Debemos instalar las correspondientes dependencias, en este caso instalar python del container de linux que correremos
RUN apt update
#Con apt update logramos primero actualizar las aplicaciones antes de instalar la version de python
RUN apt install python3 -y  


WORKDIR  /app 

COPY Script.py Leer.txt ./



CMD [ "python3","./Script.py"]

#docker build -t 2019911/docker-test:1.0.0 .