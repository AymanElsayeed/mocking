"""
abstract base class for inht

"""

from abc import ABC, abstractmethod


class A(ABC):
    class_attribute = 1

    def __init__(self, n: int):
        self.n = n

    @abstractmethod
    def add(self, n):
        pass

    @property
    def plus_one(self):
        return self.n + 1

    @plus_one.setter
    def plus_one(self, value):
        self.n = value


class B(A):
    def __init__(self, n):
        super().__init__(n)

    def add(self, n):
        self.n += n


class C:
    def __init__(self, n):
        self.n = n
        self.b = B(n)

    def mult(self, n):
        self.n *= n
