# -*- coding: utf-8 -*-

import csv
import numpy as np


class Parser():
    def __init__(self, filename: str, delimiter: str = '', target: str = 'target'):
        self.__filename: str = filename
        self.__delimiter = delimiter
        self.__csv_dialect: csv.Dialect or None = None
        self.__csv_has_header: bool = False
        self._sniff()
        self._load_csv()
        self._find_target(target.lower())

    def _sniff(self) -> None:
        with open(self.__filename, newline='') as csvfile:
            csvdata = csvfile.read(1024)
            sniffer = csv.Sniffer()
            self.__csv_dialect = sniffer.sniff(csvdata)
            self.__csv_has_header = sniffer.has_header(csvdata)

    def _load_csv(self) -> None:
        with open(file=self.__filename, mode='r') as file:
            data = None
            if self.__delimiter:
                data = list(csv.reader(file, delimiter=self.__delimiter))
            else:
                data = list(csv.reader(file, dialect=self.__csv_dialect))
            if self.__csv_has_header:
                self.Headers = data[0]
                self.Dataset = np.array(data[1:])
                return
            raise Exception('Dataset has no headers')

    def _find_target(self, target: str) -> None:
        if not target:
            raise Exception('Empty target')
        target_index = -1
        for index, column in enumerate(self.Headers):
            if column.lower() == target:
                target_index = index
                break
        if target_index < 0:
            raise Exception(
                F'Target "{target}" not found in Dataset "{self.__filename}"')
        self.Target = np.array(self.Dataset)[:, target_index]
        self.Dataset = np.delete(self.Dataset, target_index, 1)


if __name__ == '__main__':
    parser = Parser('datasets/benchmark/joga.tsv', target='joga')
    print(parser.Headers)
    print(parser.Dataset)
    print(parser.Target)
