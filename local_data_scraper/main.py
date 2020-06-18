import json
from app.scraper import TXTFile, CSVFile


def write_to_file(result: dict, path_to: str):
    with open(path_to, 'w') as f:
        json.dump(result, f)


def process_text_file(path_from, path_to):
    t = TXTFile(path_from)
    rows = t.parse('。', ['Python'])
    result = t.count_words(rows)
    write_to_file(result, path_to)


def process_csv_file(path_from, path_to):
    t = CSVFile(path_from)
    rows = t.parse('。', ['Python'])
    result = t.count_words(rows)
    write_to_file(result, path_to)


def process_by_ext(path_from, path_to):
    ext = path_from.split('.')[-1]
    if ext == 'txt':
        return process_text_file(path_from, path_to)
    if ext == 'csv':
        return process_csv_file(path_from, path_to)
    print('No such extension found.Please check your input file is one of txe, csv or html')


if '__main__' == __name__:
    process_by_ext('./wiki.txt', './wiki_count_txt.json')
    process_by_ext('./wiki.csv', './wiki_count_csv.json')
