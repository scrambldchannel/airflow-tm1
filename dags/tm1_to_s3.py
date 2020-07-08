from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook 
from hooks.tm1_hook import TM1Hook

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


dag_config = Variable.get("tm1_to_s3_example_config", deserialize_json=True)

def cube_view_to_s3(cube, view, key, bucket, **kwargs):

    # create the hook and initialise the instance of the TM1Service object
    tm1_hook = TM1Hook(tm1_conn_id="tm1_default")
    tm1_hook.init_tm1_service()

    # pull data from a view
    view_data = tm1_hook.tm1.cubes.cells.execute_view_csv(cube_name=cube, view_name=view, private=False)

    # Create the s3 hook
    s3_hook = S3Hook(aws_conn_id="s3_default")

    # write file to s3
    s3_hook.load_string(string_data=view_data, key=key, bucket_name=bucket, replace=True)

t1 = PythonOperator(
    task_id="read_from_TM1",
    python_callable=cube_view_to_s3,
    op_kwargs = {"cube":dag_config["cube"], "view":dag_config["view"], "key":dag_config["key"], "bucket":dag_config["bucket"] },
    dag=dag,
)
