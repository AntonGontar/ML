FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install apache-airflow
RUN pip3 install pandas
RUN airflow db init

RUN airflow users create \
    --username admin \
    --firstname adminov \
    --lastname borat \
    --role Admin \
    --email spidefrman@supsfderhero.org \
    --password 4870

CMD airflow standalone