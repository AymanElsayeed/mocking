"""

This module is used to test the inheritance of classes.

"""

from connection.db import PostgresConnection
from connection import r_client


class A:
    def __init__(self, n: int):
        self.n = n
        self._connection = PostgresConnection(data=n)

    def add(self, n):
        self.n += n

    def div(self, n):
        self.n /= n
        return self.n

    @property
    def connection(self) -> PostgresConnection:
        return self._connection


class B(A):
    def __init__(self, n):
        super().__init__(n)

    def sub(self, n):
        self.n -= n


class C(B):
    def __init__(self, n):
        super().__init__(n)

    def mult(self, n):
        self.n *= n
