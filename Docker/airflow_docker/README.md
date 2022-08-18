## Билд из текущей
* `docker build -t airflow .` 

## Запуск докера
* `docker run airflow`

## Запуск докера с пробросом порта с синхронизацией рабочей папки
* `docker run -p 8080:8080  --mount type=bind,source="$(pwd)"/,target=/root/airflow/dags airflow`
* `docker run -p 8080:8080  --mount type=bind,source="/Users/user/PycharmProjects/airflow_docker/"/,target=/root/airflow/dags airflow`

## Запуск докера с пробросом порта 
* `docker run -p 8080:8080  airflow - запуска докера с портами`

## Запуск cli докера
* `docker exec -it cb4bacb8c2b4 /bin/bash`

## Список докеров
* `docker ps`

## Список образов
* `docker images`

## Запуск контейнера с несколькими образами докеров (перейти в папку > запуск)
* `docker-compose up`

## Сохранение образа 
* `docker save airflow > airflow.tar`

## Копирование папки в образ (что скопировать и куда)
* `copy dags /root/airflow/`

## аспаковка образа
* `docker load < airflow.tar`
