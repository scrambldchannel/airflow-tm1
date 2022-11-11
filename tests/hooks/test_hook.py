# import pytest

from airflow_tm1.hooks.tm1 import TM1Hook

# from airflow import settings
# from airflow.models import Connection


def test_hook_init(mock_rest_service, airflow_connection):

    hook = TM1Hook()

    assert hook
