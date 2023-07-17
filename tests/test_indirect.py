from unittest import mock
from pytest import fixture


from src.inht import C, B, A, r_client
from connection.db import PostgresConnection
from connection.rredis import RedisClient


def get_data():
    return 6


class MockPostgresConnection:
    name = "MockPostgresConnection"

    def get_data(self):
        return self.name


@mock.patch("connection.db.PostgresConnection.get_data", return_value=get_data())
def test_mock_c_postgres_obj_indirect_method_1(indirect_mock):
    c = C(2)
    assert c.connection.get_data() == 6


@mock.patch.object(PostgresConnection, "get_data", return_value=99)
def test_mock_c_postgres_obj_indirect_method_2(indirect_mock):
    c = B(2)
    assert c.connection.get_data() == 99


@mock.patch.object(PostgresConnection, "get_data", return_value=145)
def test_mock_a_postgres_obj_indirect_method_1(indirect_mock):
    c = A(2)
    assert c.connection.get_data() == 145


@mock.patch.object(PostgresConnection, "get_data", return_value=MockPostgresConnection().get_data())
def test_mock_a_postgres_obj_indirect_method_2(indirect_mock):
    c = A(2)
    assert c.connection.get_data() == "MockPostgresConnection"


@mock.patch.object(RedisClient, "get_data", return_value=789)
def test_mock_redis_client_method_1(indirect_mock):
    assert r_client.get_data() == 789


@mock.patch("connection.rredis.RedisClient.get_data", return_value=450)
def test_mock_redis_client_method_2(indirect_mock):
    assert r_client.get_data() == 450
