from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    List,
    NamedTuple,
    Optional,
    Tuple,
    TypedDict,
    TypeVar,
    Union,
)

# Constants should be in uppercase
MY_CONSTANT = 1


class MyClass:
    """This is a class"""

    def __init__(self):
        self.my_variable = 1


def is_valid_date(year: int, month: int, day: int) -> bool:
    """Check if the given year, month, and day form a valid date."""
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


def day_of_week(year: int, month: int, day: int) -> str:
    """Return the day of the week for a valid date."""
    return datetime.datetime(year, month, day).strftime("%A")


def date_printer(day: int, month: int, year: int) -> None:
    """Print the date and day of the week, given day, month, and year."""
    if is_valid_date(year, month, day):
        print(f"The entered date is: {day}-{month}-{year}")
        print(f"Day of the week: {day_of_week(year, month, day)}")
    else:
        print("Invalid date")


if __name__ == "__main__":
    date_printer(12, 12, 2023)

StudentDict = Dict[str, Union[int, str]]

student_dict: StudentDict = {"name": "John", "age": 25}
print(student_dict["name"])


class Point(NamedTuple):
    x: int
    y: int


class StudentTypedDict(TypedDict):
    name: str
    age: int
    point: Point
    friends: List["StudentTypedDict"]


student1 = StudentTypedDict(name="John", age=25, point=Point(1, 2))
print(student1)


@dataclass
class StudentDataclass:
    name: str
    age: int
    grade: str


alice = StudentDataclass("Alice", 20, "A")
print(alice)

# Usage of asyncio.run should be within this guard
# if __name__ == "__main__":

#     async def main():
#         print("Hello")
#         await asyncio.sleep(1)
#         print("World")

#     asyncio.run(main())


def consume_many_types(
    num: int,
    string: str,
    boolean: bool,
    list: list,
    dict_type: dict,
    tuple_type: tuple,
    set_type: set,
    float_type: float,
) -> None:
    pass


# Using proper type annotations
any_value: Any = 1
nums: List[int] = [1, 2, 3, 4, 5]
threed_vector: Tuple[int, int, int] = (1, 2, 3)
nd_vector: Tuple[int, ...] = (1, 2, 3, 4, 5)
custom_dict: Dict[str, int] = {"a": 1, "b": 2, "c": 3}


def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name}" if name else "Hello, world!"


class Pupil(TypedDict):
    name: str
    age: int
    grade: str


pupil_1: Pupil = {"name": "John", "age": 25, "grade": "A"}


class Dot(NamedTuple):
    x: int
    y: int
    z: int


point_1: Dot = Dot(1, 2, 3)

TAddable = TypeVar("TAddable", int, float, str)


def add(a: TAddable, b: TAddable) -> TAddable:
    return a + b


# hi
