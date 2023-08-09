from pytest import fixture
from unittest import mock
from src.nfs import *
from globals import *


@fixture()
@mock.patch("tests.conftest.get_one", return_value=2)
def get_one_fixture(get_one_mock):
    one = get_one()
    return one


def init_connection():
    # c = Connection(data="this is ayman")
    class temp(Connection):
        def send_data(self):
            return 123

    c = temp()
    return c


@fixture()
@mock.patch("tests.conftest.Connection", return_value=init_connection())
def connection_object(connection_mock_1):
    connection = Connection()
    return connection


@fixture()
@mock.patch("tests.test_nfs.Connection.get_data", return_value="got message")
def connection_object_get_data(connection_mock_1):
    connection = Connection("updated message1")
    return connection.get_data()


@fixture()
@mock.patch("tests.test_nfs.Connection.get_data", return_value="send message")
def connection_object_send_data(connection_mock_1):
    connection = Connection("updated message1")
    return connection.get_data()


@fixture(name="monkeypatch_connection")
def connection_object_send_data(monkeypatch) -> Connection:
    connection = Connection("updated message1")
    monkeypatch.setattr(connection, "get_data", lambda: "send message")
    return connection


@fixture(name="monkeypatch_connection_global_data")
def connection_object_send_data(monkeypatch) -> Connection:
    monkeypatch.setattr(Connection, "global_data", 0)
    connection = Connection("updated message1")
    return connection


@fixture(name="monkeypatch_fixture_scope_session", scope="function", autouse=True)
def monkeypatch_fixture_scope_session(monkeypatch):
    monkeypatch.setattr(my_object, "value", "value")
