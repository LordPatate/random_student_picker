from argparse import ArgumentParser
from random import shuffle

from students import Student, students_from_file


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


def random_picker_session(paths: list[str]) -> None:
    students = sum((students_from_file(path) for path in paths), start=[])
    picker = Picker(students)
    quit_aliases = {
        "exit",
        "quit",
        "stop",
        "leave",
    }
    student = picker.pick()
    print(student.first_name, student.last_name)
    try:
        while input() not in quit_aliases:
            student = picker.pick()
            print(student.first_name, student.last_name)
    except EOFError:
        pass


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("paths", nargs='*')
    namespace = parser.parse_args()
    random_picker_session(namespace.paths)


if __name__ == "__main__":
    main()
