# pylint: disable=too many blank lines, W0611

# noqa: F401
from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Dict, List, NamedTuple, TypedDict, Union

# import numpy as np
# import pandas as pd

"""This is a module docstring"""


MY_VARIABLE = 1


# pylint: disable=too many blank lines (2)
class MyClass:
    """This is a class"""

    # noqa: E303
    def __init__(self):
        self.my_variable = 1


print("hello world")


def is_valid_date(year, month, day):
    """Check if the given year, month, and day form a valid date."""
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


def day_of_week(year, month, day):
    """Return the day of the week for a valid date."""
    return datetime.datetime(year, month, day).strftime("%A")


def date_printer(day, month, year):
    """Print the date and day of the week, given day, month, and year."""
    if isinstance(year, int):
        if 1 <= year <= 9999:  # Valid year range
            if isinstance(month, int):
                if 1 <= month <= 12:  # Valid month range
                    if isinstance(day, int):
                        if is_valid_date(year, month, day):
                            print(f"The entered date is: {day}-{month}-{year}")
                            print(f"Day of the week: {day_of_week(year, month, day)}")
                        else:
                            print("Invalid date: Day is out of range for the month.")
                    else:
                        print("Invalid input: Day is not an integer.")
                else:
                    print("Invalid input: Month is out of range (1-12).")
            else:
                print("Invalid input: Month is not an integer.")
        else:
            print("Invalid input: Year is out of range (1-9999).")
    else:
        print("Invalid input: Year is not an integer.")


if __name__ == "__main__":
    # Example usage
    date_printer(12, 12, 2023)


student_dict = Dict[str, Union[int, str]]

student_dict = {"name": "John", "age": 25}
print(student_dict["name"])

# student_dict["grade"] = "A"
class Point(NamedTuple):
    x: int
    y: int


bob: "student"


class student(TypedDict):
    name: str
    age: int
    point: Point
    friends: List["student"]


student1 = student(name="John", age=25, point=Point(1, 2))
print(student1)

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grade: str


# Creating an instance of Student
alice = Student("Alice", 20, "A")

# The __repr__ method is automatically generated
print(alice)  # Output: Student(name='Alice', age=20, grade='A')

# Accessing attributes
print(alice.name)  # Output: Alice


@dataclass
class Student:
    name: str
    age: int
    grade: str


# Creating an instance of Student
alice = Student("Alice", 20, "A")

# The __repr__ method is automatically generated
print(alice)  # Output: Student(name='Alice', age=20, grade='A')

# Accessing attributes
print(alice.name)  # Output: Alice

var: int = 1
var = "hi"
import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(main())


def consume_many_types(
    num: int,
    string: str,
    boolean: bool,
    list: list,
    dict: dict,
    tuple: tuple,
    set: set,
    float: float,
) -> None:
    pass


from typing import *

any_value: Any = 1

nums: List[int] = [1, 2, 3, 4, 5]
print(nums)

nums_2: List[int] = [5, 4, 3, 2, 1]
print(nums_2)

threed_vector: Tuple[int, int, int] = (1, 2, 3)

print(threed_vector)

print(threed_vector[0])

nd_vector: Tuple[int, ...] = (1, 2, 3, 4, 5)
print(nd_vector)
dict: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(dict)

itr: Iterable[int] = [1, 2, 3, 4, 5]
print(itr)

misc: List[Union[int, float, str]] = [1, 2.0, "3", 1, "k"]
print(misc)


def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, world!!"
    else:
        return f"Hello, {name}"


print(greet())


class pupil(TypedDict):
    name: str
    age: int
    grade: str


pupil_1: pupil = {"name": "John", "age": 25, "grade": "A"}
print(pupil_1)


class dot(NamedTuple):
    x: int
    y: int
    z: int


point_1: dot = dot(1, 2, 3)
print(point_1.x)

pupil_2 = pupil(name="John", age=25, grade="A")
print(pupil_2)

pupil_3: pupil = pupil(name="John", age=25, grade="A")
print(pupil_3)

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grade: str
    mark: int


alice: Student = Student("Alice", 20, "A", 100)

print(alice)

cust = Dict[str, Union[int, str]]

customer_1: cust = {"name": "John", "age": 25}
print(customer_1)


# TAddable = Union[int, float]

TAddable = TypeVar("TAddable", int, float, str)


def add(a: TAddable, b: TAddable) -> TAddable:
    return a + b


print(add(1, 2))

print(add("1", "2"))
