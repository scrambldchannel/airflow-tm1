from airflow.models import BaseOperator
from airflow_tm1.hooks.tm1 import TM1Hook

class TM1RunTIOperator(BaseOperator):
    """
    This operator runs a TI process

    :param ti_name: The TI process to run.
    :type ti_name: str
    :param tm1_conn_id: The Airflow connection used for TM1 credentials.
    :type tm1_conn_id: str
    """
    def __init__(self,
                 ti_name: str,
                 tm1_conn_id: str = "tm1_default",
                 **kwargs) -> None:

        self.ti_name = ti_name
        self.tm1_conn_id = tm1_conn_id
        self.paramaters = kwargs

    def execute(self, context):
        tm1_hook = TM1Hook(tm1_conn_id=self.tm1_conn_id)
        if tm1_hook.tm1.processes.exists(self.ti_name):
            print(f"Process {self.ti_name} executed.")
            return tm1_hook.tm1.processes.execute_with_return(self.ti_name, self.paramaters)
        else:
            print(f"Process {self.ti_name} does not exist on TM1 server {tm1_hook.tm1.server}.")
                        

