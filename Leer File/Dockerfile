#Basamos nuestra imagen en  la siguiente imagen de python 
FROM python:3.9.10-bullseye
RUN pip install --upgrade pip
#Seteamos nuestro directorio base
WORKDIR  /app 
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
#