FROM python:3.9.10-bullseye
RUN pip install --upgrade pip

WORKDIR  /app 

COPY . .

CMD ["python", "Script.py"]


#docker build -t 2019911/docker-test:1.0.0 .
#PS D:\Mi Unidad\Cursos\Docker\Python Script\N2> docker container run -v "${pwd}/data:/app/data" 2019911/docker-test:latest