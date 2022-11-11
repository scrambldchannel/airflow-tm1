from airflow_tm1.hooks.tm1 import TM1Hook

# import pytest


def test_hook_init():

    hook = TM1Hook()

    assert hook
