# -*- coding: utf-8 -*-

from csv import reader

class Parser():
    def __init__(self, filename, separator="\t"):
        self.__filename = filename
        self.__separator = separator