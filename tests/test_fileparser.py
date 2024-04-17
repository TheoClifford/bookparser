import unittest
from main import fileParser
class TestFileParser(unittest.TestCase):
    def setUp(self):
        self.fileParser = fileParser("tests/test_data/wildfell.txt")
    def test_Wordcount(self):
        self.assertEqual(self.fileParser.wordcount(), 173_657)