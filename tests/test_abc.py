"""

Test mocking classes and objects that inherit abstract classes, and direct abstract class

"""

from unittest import mock
import pytest
from src.inht_abc import *


def test_mocking_object_attribute():
    """
    mock object attribute that inherits from abstract class
    :return:
    """
    b = B(2)
    b = mock.Mock(n=991)
    assert b.n == 991


def test_mocking_a_object_property():
    """
    test mock property of class instance that inherited from abstract class
    :return:
    """
    b = B(2)
    b = mock.Mock(plus_one=991)
    assert b.plus_one == 991


def test_mocking_an_object_instance_object():
    """
    mock object attribute that object that inherits from abstract class
    :return:
    """
    c = C(2)
    c = mock.Mock(b=991)
    assert c.b == 991


def test_nested_mock():
    """
    test nested mock, mock object attribute that object that inherits from abstract class
    :return:
    """
    c = C(2)
    c.b = mock.Mock(plus_one=991)
    assert c.b.plus_one == 991


def test_mocking_nested_object_class_attribute():
    c = C(2)
    c.b.class_attribute = 99
    c.b = mock.Mock(plus_one=991, class_attribute=1010)
    assert c.b.class_attribute == 1010
    c2 = C(2)
    assert c2.b.class_attribute == 1
    A.class_attribute = 8090
    c3 = C(3)
    assert c2.b.class_attribute == 8090
