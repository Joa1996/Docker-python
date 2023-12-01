#Basamos nuestra imagen en  la siguiente imagen de python 
FROM python:3.9.10-bullseye
RUN pip install --upgrade pip
#Definimo la variable de entorno para poder crear un container con el nombre de archivo que querramos
ENV file_value='File.csv' 
#por defecto definimos el valor de File.csv
#Seteamos nuestro directorio base
WORKDIR  /app 
COPY requirements.txt ./
#Intalamos las librerias necesarias del archivo "requirements.txt"
RUN pip install --no-cache-dir -r requirements.txt

#Copíamos todos los archivos al directorio raiz, en este caso solamente el archivo "Script.py"

COPY . .

CMD ["python", "Script.py"]


#docker build -t 2019911/docker-test:1.0.0 .
#PS D:\Mi Unidad\Cursos\Docker\Python Script\N2> docker container run -v "${pwd}/data:/app/data" 2019911/docker-test:latest

# Cuando creemos el Container, en la ruta donde creemos el containe debemos crear una
# carpeta que tendra el archivo a procesar por el script python, la carpeta debera llamarse "data".
# Luego creamos un bind volume que usara nuestra ruta local como 
# la ruta de la imagen, y de esta forma procesara el archivo
#
# Con este comando creamos el container y le pasamos el  valor de la variable que tendra el nombre del archivo
#  docker container run -v "${pwd}/data:/app/data" -e "file_value=Segundo.csv" 2019911/docker-test:1.0.0