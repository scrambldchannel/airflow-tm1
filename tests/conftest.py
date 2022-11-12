import pytest

# from TM1py import Cube, Dimension, DimensionService, Element, Hierarchy
from TM1py.Services.RestService import RestService

# from airflow.models.connection import Connection


@pytest.fixture(scope="function")
def airflow_connection():

    # conn = Connection(
    #     conn_id="tm1_default",
    #     host="localhost",
    #     login="admin",
    #     password="apple",
    #     port=10001,
    #     extra="""{"ssl":false}""",
    # )

    # return conn
    pass


@pytest.fixture(scope="function")
def mock_rest_service(module_mocker):
    """
    Simple mock of TM1py's low level rest service
    """

    # These were necessary to get this working
    module_mocker.patch.object(RestService, "_start_session", return_value=True)
    module_mocker.patch.object(RestService, "set_version", return_value="testing version")

    # It probably makes senese to mock other things like this
    module_mocker.patch.object(RestService, "is_connected", return_value=None)

    # set some necessary kwargs
    mock_args = {"address": "localhost", "port": 8080}

    return RestService(**mock_args)


# @pytest.fixture(scope="module")
# def mock_dim_service(module_mocker, mock_rest_service, dims_all):
#     """
#     Simple mock of TM1py's dimension service
#     """

#     # weird thing here where I find I need to add a param to the function
#     # should I be passing some sort of mock thing?
#     def get_all_names(none):
#         return [d.name for d in dims_all]

#     module_mocker.patch.object(DimensionService, "get_all_names", new=get_all_names)

#     return DimensionService(mock_rest_service)
