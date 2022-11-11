from airflow import DAG
from airflow.utils.dates import days_ago

from airflow_tm1.operators.tm1_run_ti import TM1RunTIOperator

default_args = {
    "owner": "Airflow",
    "start_date": days_ago(2),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "you@somewhere.com",
    "retries": 1,
}

with DAG(dag_id="example_run_ti", default_args=default_args, schedule_interval="@daily") as dag:

    t1 = TM1RunTIOperator(
        task_id="run_ti",
        process_name="Refresh Feeders",
        parameters={"pCube": "Capital"},
        dag=dag,
    )

    t1
