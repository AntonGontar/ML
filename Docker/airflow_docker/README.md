#билд из текущей 
docker build -t airflow . 

#Запуск докера с пробросом порта с синхронизацией рабочей папки
docker run -p 8080:8080  --mount type=bind,source="$(pwd)"/,target=/root/airflow/dags airflow
docker run -p 8080:8080  --mount type=bind,source="/Users/user/PycharmProjects/airflow_docker/"/,target=/root/airflow/dags airflow

#Запуск докера с пробросом порта 
docker run -p 8080:8080  airflow - запуска докера с портами

#запуск cli докера
docker exec -it cb4bacb8c2b4 /bin/bash

#список докеров
docker ps

#запуск контейнера с несколькими образами докеров (перейти в папку > запуск)
docker-compose up

#сохранение образа 
docker save airflow > airflow.tar

#копирование папки в образ (что скопировать и куда)
copy dags /root/airflow/

#распаковка образа
docker load < airflow.tar

#список образов
docker images

docker run airflow