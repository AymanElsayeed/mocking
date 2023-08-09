"""

This file is used to demonstrate the monkey patching functionality of pytest.

"""
from src import *
from src.inht import *


def test_mocked_value(monkeypatch):
    monkeypatch.setitem(globals(), "CUSTOM_GLOBAL_ENV_VAR", "100")
    assert CUSTOM_GLOBAL_ENV_VAR == "100"


def test_original_value():
    assert CUSTOM_GLOBAL_ENV_VAR == "ayman"


def test_class_a_setattr(monkeypatch):
    a = A(2)
    monkeypatch.setattr(a, "n", 100)
    assert a.n == 100


def test_1(monkeypatch_connection):
    assert monkeypatch_connection.get_data() == "send message"


def test_2(monkeypatch_connection_global_data):
    assert monkeypatch_connection_global_data.global_data == 0


def test_class_a_add_setattr(monkeypatch):
    a = A(2)
    a.extra = -1
    monkeypatch.setattr(a, "extra", 100)
    assert a.extra == 100