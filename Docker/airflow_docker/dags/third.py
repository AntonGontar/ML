from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import numpy as np
from pytrends.request import TrendReq
import os


third_dag=DAG("third_dag",
        start_date=days_ago(0,0,0,0,0)
        )

def get_random_trend_in_country(country):
    try:
        pytrend = TrendReq()
        country_trends = pytrend.trending_searches(pn=country)
        country_trends['country'] = country

        df = country_trends.reset_index(drop=False)
        df = df.rename(columns={0: 'search_term', 'index': 'order'})

        # search popularity (top 10)
        rank = np.random.random_integers(0, 10)
        d = df[df.order == rank][['search_term', 'country']].set_index('country').T.to_dict('records')[0]
        return d
    except Exception as e:
        error = str(e)
        print(error)

download_dataframe = PythonOperator(
    task_id='get_random_trend_in_country',
    python_callable = get_random_trend_in_country(country='russia'),
    dag = third_dag
)

os.chdir("/")

download_dataframe
