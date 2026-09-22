import csv
from typing import NamedTuple


class Student(NamedTuple):
    login: str
    first_name: str
    last_name: str
    email: str
    uid: str


def snake_case(name: str) -> str:
    return name.strip().lower().replace(" ", "_")


def students_from_file(csv_file_name: str) -> list[Student]:
    with open(csv_file_name, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            Student(**{
                snake_case(field_name): value
                for field_name, value in row.items()
                if field_name.strip() != ""
            })
            for row in reader
        ]
