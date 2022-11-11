from operator import gt

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago, timedelta

from airflow_tm1.sensors.tm1_cell_value import TM1CellValueSensor

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(dag_id="example_value_sensor", default_args=default_args) as dag:

    t1 = TM1CellValueSensor(
        task_id="check_value",
        # check every 15 minutes
        poke_interval=60 * 15,
        # timeout in 12 hours
        timeout=60 * 60 * 12,
        tm1_conn_id="tm1_default",
        cube="Task Workflow",
        value=1,
        elements="OPEX,Total Company,Complete",
        # apply the greater than operator
        op=gt,
    )

    t2 = DummyOperator(task_id="do_nothing")

    t1 >> t2
