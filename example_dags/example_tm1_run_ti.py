from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago, timedelta

from airflow_tm1.operators.tm1_run_ti import TM1RunTIOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "schedule_interval": "@daily",
}

dag = DAG(
    dag_id="example_tm1_run_ti",
    default_args=default_args,
)

t1 = TM1RunTIOperator(
    task_id="getTaeFuck",
    process_name="Refresh Feeders",
    parameters={"pCube": "Capital"},
    dag=dag,

)
