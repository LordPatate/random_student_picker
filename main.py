import csv
from argparse import ArgumentParser
from random import shuffle
from typing import NamedTuple


class Student(NamedTuple):
    login: str
    first_name: str
    last_name: str
    email: str
    uuid: str


def students_from_file(csv_file_name: str) -> list[Student]:
    with open(csv_file_name, newline="") as csv_file:
        reader = csv.reader(csv_file)
        return [Student._make(row[:len(Student._fields)]) for row in reader]


class Picker:
    def __init__(self, students: list[Student]) -> None:
        self._list = students.copy()
        shuffle(self._list)
        self._index: int = 0

    def pick(self, n: int = 1) -> Student:
        student = self._list[self._index]
        self._index += 1
        if self._index >= len(self._list):
            shuffle(self._list)
            self._index = 0
        return student


def random_picker_session(file_name: str) -> None:
    picker = Picker(students_from_file(file_name))
    quit_aliases = {
        "exit",
        "quit",
        "stop",
        "leave",
    }
    student = picker.pick()
    try:
        while input() not in quit_aliases:
            student = picker.pick()
            print(student.first_name, student.last_name)
    except EOFError:
        pass


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("file_name")
    namespace = parser.parse_args()
    random_picker_session(namespace.file_name)


if __name__ == "__main__":
    main()
