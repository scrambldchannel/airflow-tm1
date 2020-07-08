from airflow.hooks.base_hook import BaseHook
from airflow.exceptions import AirflowException
from TM1py.Services import TM1Service


class TM1Hook(BaseHook):
    """
    Interact with IBM Cognos TM1, using the TM1py library.
    """

    def __init__(self, tm1_conn_id='tm1_default', **kwargs):

        self.tm1_conn_id = tm1_conn_id
        self.connection = self.get_connection(tm1_conn_id)

        self.config = {
            "address" : self.connection.host,
            "port" : self.connection.port,
            "user" : self.connection.login,
            "password" : self.connection.password,
            "ssl" : self.connection.extra_dejson['ssl']
        }

    def init_tm1_service(self):
        self.tm1 = TM1Service(**self.config)
        server_version = self.tm1.server.get_product_version()
        server_name = self.tm1.server.get_server_name()
        print(f"Cnnected to TM1 server {server_name} which is running version {server_version}")