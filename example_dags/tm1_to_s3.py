from airflow import DAG
from airflow.hooks.S3_hook import S3Hook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago, timedelta

from airflow_tm1.hooks.tm1 import TM1Hook

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "schedule_interval": "@daily",
}

dag = DAG(
    dag_id="tm1_to_s3_example",
    default_args=default_args,
)

#dag_config = Variable.get("tm1_to_s3_example_config", deserialize_json=True)


def cube_view_to_s3(cube, view, **kwargs):

    # create the hook and initialise the instance of the TM1Service object
    tm1_hook = TM1Hook(tm1_conn_id="tm1_default")

    tm1 = tm1_hook.get_conn()

    # pull data from a view
    view_data = tm1.cubes.cells.execute_view_csv(
        cube_name=cube, view_name=view, private=False)
    #s3_hook = S3Hook(aws_conn_id="s3_default")

    # write file to s3
 #   s3_hook.load_string(string_data=view_data, key=key, bucket_name=bucket, replace=True)


t1 = PythonOperator(
    task_id="read_from_TM1",
    python_callable=cube_view_to_s3,
    op_kwargs={"cube": "Revenue", "view": "zExport Data"},
    dag=dag,
)
