from airflow import DAG
from airflow.hooks.S3_hook import S3Hook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from airflow_tm1.hooks.tm1 import TM1Hook

default_args = {
    "owner": "Airflow",
    "start_date": days_ago(2),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "you@somewhere.com",
    "retries": 1,
}


def cube_view_to_s3(cube, view, bucket, key, **kwargs):

    tm1_hook = TM1Hook(tm1_conn_id="tm1_default")
    tm1 = tm1_hook.get_conn()

    view_data = tm1.cubes.cells.execute_view_csv(cube_name=cube, view_name=view, private=False)

    s3_hook = S3Hook(aws_conn_id="s3_default")
    s3_hook.load_string(string_data=view_data, key=key, bucket_name=bucket, replace=True)


with DAG(dag_id="example_tm1_to_s3", schedule_interval="@daily", default_args=default_args) as dag:

    t1 = PythonOperator(
        task_id="view_to_S3",
        python_callable=cube_view_to_s3,
        op_kwargs={
            "cube": "Income Statement Reporting",
            "view": "Income Statement - Management",
            "key": "airflow-test/{{ ds_nodash }}.csv",
            "bucket": "scrambldbucket",
        },
        dag=dag,
    )

    t1
