from airflow_tm1.operators.tm1_run_chore import TM1RunChoreOperator
from airflow_tm1.operators.tm1_run_ti import TM1RunTIOperator

# import pytest


def test_run_ti_init():

    process = "Refresh_Feeders"

    op = TM1RunTIOperator(process_name=process, task_id=process)
    assert op


def test_run_chore_init():

    chore = "Backup"
    op = TM1RunChoreOperator(chore_name=chore, task_id=chore)
    assert op
