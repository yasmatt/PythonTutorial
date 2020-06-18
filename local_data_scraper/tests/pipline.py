import unittest
from local_data_scraper.app.pipeline import split_by_stop_word_from_str, find_target_words, count_by_target_word
from local_data_scraper.app.scraper import TXTFile, CSVFile


class TestPipeline(unittest.TestCase):
    def test_split_by_stop_word(self):
        data = 'これはですとです。Pythonのテスト。Python未経験。'
        _data = split_by_stop_word_from_str(data, '。')
        self.assertEqual(_data, ['これはですとです', 'Pythonのテスト', 'Python未経験'])

    def test_find_target_words(self):
        data = 'これはですとです。Pythonのテスト。Python未経験。'
        _data = split_by_stop_word_from_str(data, '。')
        result = find_target_words(_data, ['Python'])
        expected = [['Python'], ['Python']]
        self.assertEqual(result, expected)

    def test_count_by_target_word(self):
        data = 'これはですとです。Pythonのテスト。Python未経験。'
        _data = split_by_stop_word_from_str(data, '。')
        result = count_by_target_word(find_target_words(_data, ['Python']))
        expected = {'Python': 2}
        self.assertEqual(result, expected)


class TestFileType(unittest.TestCase):
    def test_text_file(self):
        path = './wiki.txt'
        t = TXTFile(path)
        rows = t.parse('。', ['Python'])
        result = t.count_words(rows)
        expected = {
            'Python': 2
        }
        self.assertEqual(result, expected)

    def test_csv_file(self):
        path = './wiki.csv'
        t = CSVFile(path)
        rows = t.parse('。', ['Python'])
        result = t.count_words(rows)
        expected = {
            'Python': 2
        }
        self.assertEqual(result, expected)


if '__main__' == __name__:
    unittest.main()
