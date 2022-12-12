"""

inheritance mocking test cases examples

"""

from unittest import mock
from unittest.mock import MagicMock, PropertyMock
import pytest
import src.inht
from src.inht import *


def my_dev():
    return 11


def my_dev2():
    return 1


@mock.patch("tests.test_inht.A", return_value=MagicMock(n=991))
def test_mock_instance_attribute(m):
    """
    test mock instance attribute
    :param m:
    :return:
    """
    a = A(2)
    assert a.n == 991


def test_mock_instance_property(mocker):
    """
    test mock instance property
    :param mocker:
    :return:
    """
    expected = 991
    mocker.patch.object(src.inht.A, 'connection', expected)
    a = A(2)
    assert a.connection == expected


@mock.patch("tests.test_inht.A.div", return_value=my_dev())
def test_mocking_a_object_function_div_method_1(div_mock):
    """
    test A.div method
    :param div_mock:
    :return:
    """
    a = A(2)
    assert a.div(0) == 11


@mock.patch.object(A, "div", return_value=99)
def test_mocking_a_object_function_div_method_2(div_mock):
    """
    test A.div method
    :param div_mock:
    :return:
    """
    a = A(2)
    assert a.div(0) == 99


@mock.patch("tests.test_inht.A.div", return_value=my_dev())
def test_a_div_oringinal(div_mock):
    a = A(0)
    assert a.div(0) == 11


@mock.patch("tests.test_inht.A.div", return_value=my_dev2())
def test_b_div(div_mock):
    a = B(2)
    assert a.div(0) == 1


@mock.patch("tests.test_inht.C.div", return_value=my_dev2())
def test_multi_1(div_mock):
    a = C(2)
    assert a.div(0) == 1


@mock.patch("tests.test_inht.C.div", return_value=my_dev2())
def test_multi_2(div_mock):
    a = A(2)
    with pytest.raises(ZeroDivisionError):
        assert a.div(0) == 1


@mock.patch("tests.test_inht.C.div", return_value=my_dev2())
def test_mock_c_div(div_mock):
    a = B(2)
    # because B.div is not mocked, and B.div calls A.div
    # so A.div will be called
    # the mock useless in this case
    with pytest.raises(ZeroDivisionError):
        assert a.div(0) == 1


@mock.patch("tests.test_inht.B.div", return_value=my_dev2())
def test_mock_b_div(div_mock):
    # because B.div is mocked, so C.div will be mocked too
    # because C does not have div method, so it will get it from B
    a = C(2)
    assert a.div(0) == 1


def test_mock_an_object_property_method_1():
    """
    test mock an object
    :return:
    """
    a = A(2)
    a._connection = MagicMock()
    a._connection.get_data.return_value = 99
    assert a.connection.get_data() == 99


def test_mock_an_object_property_method_2():
    """
    test mock an object
    :return:
    """
    a = A(2)
    a._connection = MagicMock(get_data=MagicMock(return_value=1099))
    assert a.connection.get_data() == 1099
