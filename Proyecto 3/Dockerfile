FROM python:3.9.10-bullseye
RUN pip install --upgrade pip
WORKDIR /handle_data
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "handle_data.py" ]
#docker container run  -v "${pwd}/data:/handle_data/data"  2019911/docker-test:latest