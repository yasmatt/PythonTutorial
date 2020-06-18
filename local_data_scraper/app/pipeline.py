from collections import Counter
import itertools


# split by the stop word
# find the target word in each row
# count each target word

def split_by_stop_word_from_str(raw_data: str, stop_word: str) -> list:
    _data = [row.split(stop_word) for row in raw_data.splitlines()]
    return [r for r in itertools.chain.from_iterable(_data) if r]


def split_by_stop_word_from_nested_list(raw_data: list, stop_word: str) -> list:
    rows = [r.split(stop_word) for row in raw_data for r in row if r]
    return itertools.chain.from_iterable(rows)


def find_target_words(rows: list, target_words: list) -> list:
    def _filter(_row: str, _words: list) -> list:
        return [_w for _w in _words if _w in _row]

    return list(filter(None, [_filter(row, target_words) for row in rows]))


def count_by_target_word(filtered_data: list) -> dict:
    counter = Counter()
    for row in itertools.chain.from_iterable(filtered_data):
        counter[row] += 1
    return dict(counter)
