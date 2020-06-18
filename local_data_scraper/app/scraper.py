import abc
import csv
from app.pipeline import split_by_stop_word_from_nested_list, split_by_stop_word_from_str, \
    find_target_words, count_by_target_word


class Logic(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def split_by_stop_word(cls, raw_data: str, stop_word: str):
        raise NotImplementedError

    @staticmethod
    def find_target_words(rows: list, words: list) -> list:
        return find_target_words(rows, words)

    @staticmethod
    def count_by_target_word(filtered_data: list) -> dict:
        return count_by_target_word(filtered_data)


class FileType(metaclass=abc.ABCMeta):
    def __init__(self, file_path: str):
        self.file_path = file_path

    _logic = Logic

    @abc.abstractmethod
    def read(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def parse(self, stop_word: str, target_words: list) -> str:
        raise NotImplementedError

    @staticmethod
    def count_words(rows: list) -> dict:
        return count_by_target_word(rows)


class TXTFile(FileType):
    class TxtLogic(Logic):
        @classmethod
        def split_by_stop_word(cls, raw_data: str, stop_word: str):
            return split_by_stop_word_from_str(raw_data, stop_word)

    _logic = TxtLogic

    def __init__(self, file_path):
        super(TXTFile, self).__init__(file_path)

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def parse(self, stop_word: str, target_words: list) -> list:
        raw_data = self.read()
        return find_target_words(
            self._logic.split_by_stop_word(raw_data, stop_word),
            target_words
        )


class CSVFile(FileType):
    class CsvLogic(Logic):
        @classmethod
        def split_by_stop_word(cls, raw_data: list, stop_word: str):
            return split_by_stop_word_from_nested_list(raw_data, stop_word)

    _logic = CsvLogic

    def __init__(self, file_path):
        super(CSVFile, self).__init__(file_path)

    def read(self):
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def parse(self, stop_word: str, target_words: list) -> list:
        raw_data = self.read()
        r = find_target_words(
            self._logic.split_by_stop_word(raw_data, stop_word),
            target_words
        )
        return r
