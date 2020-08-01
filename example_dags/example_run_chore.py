from airflow import DAG
from airflow.utils.dates import days_ago, timedelta

from airflow_tm1.operators.tm1_run_chore import TM1RunChoreOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "schedule_interval": "@daily",
}

dag = DAG(
    dag_id="example_run_chore",
    default_args=default_args,
)

t1 = TM1RunChoreOperator(
    task_id="trigger_cache_views",
    chore_name="cache_views",
    dag=dag,
)
