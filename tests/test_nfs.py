from src.nfs import *
from unittest import mock


@mock.patch("tests.test_nfs.get_one", return_value=2)
def test_f_1(get_one_mock):
    one = get_one()
    assert one == 2


def test_mocked_function_1(get_one_fixture):
    assert get_one_fixture == 2


@mock.patch("tests.test_nfs.get_one", return_value=22)
def test_mocked_function_2():
    one = get_one()
    assert one == 22


def test_mocker_connection_object(connection_object):
    # assert connection_object.send_data() == "this is ayman"
    assert connection_object.send_data() == 123


@mock.patch("tests.test_nfs.Connection.send_data", return_value="updated message")
def test_mocker_object_method_1(connection_mock):
    connection = Connection()
    assert connection.send_data() == "updated message"


def test_mocker_object_method_2(connection_object_get_data):
    assert connection_object_get_data == "got message"


def test_mocker_object_method_3(connection_object_send_data):
    assert connection_object_send_data == "send message"


@mock.patch("tests.test_nfs.Connection.global_data", return_value="updated message2")
def test_f_3(connection_mock):
    connection = Connection()
    assert connection.get_global_data().return_value == "updated message2"


@mock.patch("tests.test_nfs.Connection.get_global_data", return_value="wow")
def test_f_4(connection_mock):
    connection = Connection()
    assert connection.get_global_data() == "wow"
