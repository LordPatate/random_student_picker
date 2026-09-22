from argparse import ArgumentParser
from pathlib import Path

from students import Student, students_from_file


def first_names_frequencies(directory: str) -> list[tuple[str, int]]:
    first_names: dict[str, int] = {}
    for csv_file in Path(directory).glob("*.csv"):
        for student in students_from_file(csv_file):
            first_names[student.first_name] = 1 + first_names.get(student.first_name, 0)
    return sorted(first_names.items(), key=lambda name_freq: name_freq[1], reverse=True)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("-n", type=int, default=-1)
    namespace = parser.parse_args()
    for first_name, count in first_names_frequencies(namespace.directory)[:namespace.n]:
        print(f"{first_name}: {count}")


if __name__ == "__main__":
    main()
