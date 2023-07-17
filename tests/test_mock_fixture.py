import pytest
from pytest import fixture
from unittest import mock

from src.inht import C, B, A, r_client
from connection.db import PostgresConnection
from connection.rredis import RedisClient


@fixture()
def mock_postgres_connection_method_1():
    with mock.patch.object(PostgresConnection, "get_data", return_value=99):
        a = A(2)
        yield a


@fixture()
def mock_postgres_connection_method_2():
    with mock.patch("connection.db.PostgresConnection.get_data", return_value=147):
        a = A(2)
        yield a


@fixture()
def nested_mock():
    with mock.patch.object(PostgresConnection, "get_data", return_value=99):
        with mock.patch.object(RedisClient, "get_data", return_value=789):
            a = A(2)
            yield a


@fixture(params=[(A, 110), (B, 120), (C, 130)])
def nested_parametrized_mock_objects_method_1(request):
    cls_obj, value = request.param
    with mock.patch.object(PostgresConnection, "get_data", return_value=value):
        with mock.patch.object(RedisClient, "get_data", return_value=value):
            yield cls_obj(value), value


@fixture(params=[(A, 210), (B, 220), (C, 230)])
def nested_parametrized_mock_objects_method_2(request):
    cls_obj, value = request.param
    with mock.patch("connection.db.PostgresConnection.get_data", return_value=value):
        with mock.patch("connection.rredis.RedisClient.get_data", return_value=value):
            yield cls_obj(value), value


def test_mock_a_postgres_obj_indirect_method_1(mock_postgres_connection_method_1):
    assert mock_postgres_connection_method_1.connection.get_data() == 99


def test_mock_a_postgres_obj_indirect_method_2(mock_postgres_connection_method_2):
    assert mock_postgres_connection_method_2.connection.get_data() == 147


def test_nested_mock(nested_mock):
    assert nested_mock.connection.get_data() == 99
    assert r_client.get_data() == 789


def test_nested_parametrized_mock_method_1(nested_parametrized_mock_objects_method_1):
    cls_obj, value = nested_parametrized_mock_objects_method_1
    assert cls_obj.connection.get_data() == value
    assert r_client.get_data() == value


def test_nested_parametrized_mock_method_2(nested_parametrized_mock_objects_method_2):
    cls_obj, value = nested_parametrized_mock_objects_method_2
    assert cls_obj.connection.get_data() == value
    assert r_client.get_data() == value
