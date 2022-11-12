# from airflow.hooks.base import BaseHook
from TM1py.Services import TM1Service


class TM1Hook:
    """
    Interact with IBM Cognos TM1, using the TM1py library.
    """

    def __init__(self) -> None:
        """
        A hook that uses TM1py to connect to a TM1 database.
        :param tm1_conn_id: The name of the TM1 connection to use.
        :type tm1_conn_id: str
        """

        self.tm1_conn_id: str = None
        self.tm1: TM1Service = None

        # connection params
        # think about how to structure this
        self.address = None
        self.port = None
        self.user = None
        self.password = None
        self.db = None
        self.server_version = None

    # def init(self, **kwargs):

    #     # Set a default for session context for easier identification in TM1top etc.

    #     # check for relevant additional parameters in conn.extra
    #     # except session_id as not sure if this makes sense in an Airflow context
    #     # extra_arg_names = [
    #     #     "base_url",
    #     #     "decode_b64",
    #     #     "namespace",
    #     #     "ssl",
    #     #     "session_context",
    #     #     "logging",
    #     #     "timeout",
    #     #     "connection_pool_size",
    #     # ]

    #     pass
    #     # extra_args = {name: val for name, val in conn.extra_dejson.items() if name in extra_arg_names}

    #     # if "session_context" not in kwargs:
    #     #     kwargs["session_context"] = "Airflow"

    #     # self.tm1 = TM1Service(
    #     #     address=self.address, port=self.port, user=self.user, password=self.password, **extra_args
    #     # )

    # def init_from_connection(self, connection: str) -> TM1Service:
    #     """
    #     Uses the connection details to create and return an instance of a TM1Service object.
    #     :return: TM1Service
    #     """

    #     conn = connection
    #     self.address = conn.host
    #     self.port = conn.port
    #     self.user = conn.login
    #     self.password = conn.password

    #     # self.tm1 = TM1Service(
    #     #     address=self.address, port=self.port, user=self.user, password=self.password, **extra_args
    #     # )

    #     # self.db = self.tm1.server.get_server_name()
    #     # self.server_version = self.tm1.server.get_product_version()

    #     # return self.tm1
