from airflow.hooks.base_hook import BaseHook
from airflow.exceptions import AirflowException
from TM1py.Services import TM1Service

class TM1Hook(BaseHook):
    """
    Interact with IBM Cognos TM1, using the TM1py library.
    """

    def __init__(self, tm1_conn_id='tm1_default'):
        """
        Prepares hook to connect to a TM1 database.
        :param tm1_conn_id: The name of the TM1 connection to use.
        :type tm1_conn_id: str
        """
        self.tm1_conn_id = tm1_conn_id
        self.conn = self.get_connection(self.tm1_conn_id)
        self.address = self.conn.host
        self.port = self.conn.port
        self.user = self.conn.login
        self.password = self.conn.password
        self.ssl = self.conn.extra_dejson['ssl']
        self.tm1 = TM1Service(
            address=self.address,
            port=self.port,
            user=self.user,
            password=self.password,
            ssl=self.ssl
        )
        self.db = self.tm1.server.get_server_name()
        self.server_version = self.tm1.server.get_product_version()