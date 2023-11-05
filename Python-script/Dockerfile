FROM ubuntu:latest  
#Heredados de ubuntu los objetos necesarios para correr un python script en este caso de ubunto/Linux


#Debemos instalar las correspondientes dependencias, en este caso instalar python del container de linux que correremos
RUN apt update
#Con apt update logramos primero actualizar las aplicaciones antes de instalar la version de python
RUN apt install python3 -y  


WORKDIR  /app 

COPY print.py ./

CMD [ "python3","./print.py"]