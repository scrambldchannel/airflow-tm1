import unittest

from airflow import settings
from airflow.models import Connection

from airflow_tm1.hooks.tm1 import TM1Hook


class TestTM1Hook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create the connection but don't commit it
        conn = Connection(
            conn_id="tm1_default",
            host="localhost",
            login="admin",
            password="apple",
            port=10001,
            extra="""{"ssl":false}""",
        )
        session = settings.Session()
        session.add(conn)

    def test_create_hook(self):
        hook = TM1Hook(tm1_conn_id="tm1_default")
        self.assertEqual(hook.tm1_conn_id, "tm1_default")
        self.assertIsNone(hook.tm1)
        self.assertIsNone(hook.address)
        self.assertIsNone(hook.port)
        self.assertIsNone(hook.user)
        self.assertIsNone(hook.password)
        self.assertIsNone(hook.db)
        self.assertIsNone(hook.server_version)

    @classmethod
    def tearDownClass(cls):
        # I don't think there is anything to tear down because the connection wasn't committed
        pass
