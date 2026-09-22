import csv
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
