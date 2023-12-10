FROM python:3.9.10-bullseye

RUN pip install --upgrade pip

WORKDIR  /app 
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "Script_Lite.py"]



#Esta imagen lo que hara sera  crear una imagen en la que nosotros
# leeremos un archivo que querramos y 
# automaticamente almacenaremos el contenido en una BD de SQL Lite
#
#
#