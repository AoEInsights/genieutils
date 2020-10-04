import csv
from typing import Dict


def load_txt(path: str) -> Dict[int, str]:
    strings = dict()

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ", quotechar='"')

        for row in csv_reader:
            if len(row) == 2:
                try:
                    strings[int(row[0])] = row[1]
                except ValueError:
                    pass

    return strings
