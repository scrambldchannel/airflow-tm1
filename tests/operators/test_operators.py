# import pytest

from airflow_tm1.operators.tm1_run_chore import TM1RunChoreOperator
from airflow_tm1.operators.tm1_run_ti import TM1RunTIOperator

# from airflow import settings
# from airflow.models import Connection


def test_run_ti_init(mock_rest_service, airflow_connection):

    process = "Refresh_Feeders"

    op = TM1RunTIOperator(process_name=process, task_id=process)
    assert op


def test_run_chore_init(mock_rest_service, airflow_connection):

    chore = "Backup"
    op = TM1RunChoreOperator(chore_name=chore, task_id=chore)
    assert op
