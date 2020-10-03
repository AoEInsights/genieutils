import csv


class Txt:
    def __init__(self, path: str):
        self.strings = dict()

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=" ", quotechar='"')

            for row in csv_reader:
                if len(row) == 2:
                    try:
                        self.strings[int(row[0])] = row[1]
                    except ValueError:
                        pass
