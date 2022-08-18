from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import pandas as pd
import os

second_dag=DAG("second_dag",
        start_date=days_ago(0,0,0,0,0)
        )

def download_titanic_dataset():
    df = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
    df.to_csv ("df.csv")

download_dataframe = PythonOperator(
    task_id='download_titanic_dataset',
    python_callable=download_titanic_dataset,
    dag=second_dag)

def transform_titanic_dataset():
    df = pd.read_csv("df.csv")
    del df['Unnamed: 0']
    gr = df.groupby("Pclass").agg({"Survived": "mean"})
    gr.to_csv ("output.csv")


transform_dataframe = PythonOperator(
    task_id='transform_titanic_dataset',
    python_callable=transform_titanic_dataset,
    dag=second_dag
    )


os.chdir("/")


download_dataframe >> transform_dataframe

