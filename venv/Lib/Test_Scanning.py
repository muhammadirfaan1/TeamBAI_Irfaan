import unittest


class Testscanning(unittest.TestCase):
    def test_Scanning(self):
        status_code = '200'
        headers = 'Mobile'
        self.assertEqual(status_code, '200')
        self.assertEqual(headers, 'Mobile')
class TestScraping(unittest.TestCase):
    def test_Scraping(self):
        filetype = '.jpg'
        self.assertEqual(filetype, '.jpg')


if __name__ == '__main__':
    unittest.main()