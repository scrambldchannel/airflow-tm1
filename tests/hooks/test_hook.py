import pytest

# from airflow import settings
# from airflow.models import Connection

# from airflow_tm1.hooks.tm1 import TM1Hook


@pytest.fixture(scope="function")
def mock_airflow_connection():
    # Create the connection but don't commit it

    return "frog"

    # conn = Connection(
    #     conn_id="tm1_default",
    #     host="localhost",
    #     login="admin",
    #     password="apple",
    #     port=10001,
    #     extra="""{"ssl":false}""",
    # )

    # return conn


def test_hook(mock_rest_service, mock_airflow_connection):

    pass
    # hook = TM1Hook(tm1_conn_id="tm1_default")

    # assert hook.tm1_conn_id, "tm1_default"
    # assert hook.address is None
