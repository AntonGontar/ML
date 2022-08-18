from airflow import DAG
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime

dag=DAG("first_dag",
        start_date=days_ago(0,0,0,0,0)
        )

operation_1 = BashOperator(
    bash_command="pwd",
    task_id="operation_1",
    dag=dag
)

operation_2 = BashOperator(
    bash_command="sleep 5",
    task_id="operation_2",
    dag=dag
)

operation_3 = BashOperator(
    bash_command="sleep 20",
    task_id="operation_3",
    dag=dag
)

operation_4 = BashOperator(
    bash_command="""echo "completed" """,
    task_id="operation_4",
    dag=dag
)
operation_1 >> [operation_2,operation_3]
[operation_2,operation_3] >> operation_4