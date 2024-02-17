# for advanced types
from typing import List, TypeVar, Generic, Union, Optional, Any
from pathlib import Path

# Python is Dynamic

# Type hint

x: int = 10  # ==>>  Check type compatibility with "mypy"
name: str = 'AmiR'


def open_file(addrs: Union[str, Path]) -> None:
    pass


# Union[str, None] => Optional[str]
def greet(name: Optional[str]) -> str:
    return f"HEllO, {name}"


# Comman Type : int, str, float, Bool

def scale(scaler: int, vector: List[float]) -> List[float]:
    return [scaler * num for num in vector]


# Because that complex data type can reduce code readibility, we can define "alias" for this problem :
### Alias :
Vector = List[float]


def scale(scaler: int, vector: Vector) -> Vector:
    return [scaler * num for num in vector]


# Gradual Typing : ignore where annotation is not defind and check only code annotations


# Generic : all of element be same
T = TypeVar("T")


def first(lst: T) -> T:
    return lst[0]


class Stack(Generic[T]):
    def __init__(self):
        self.st = []

    def push(self, element: T) -> None:
        self.st.append(element)
