import unittest
import main

class TestParserProgram(unittest.TestCase):    
    def test_return_file_content(self):
        self.assertIsInstance(main.return_file_content('raw_data.txt'), list, msg="FileNameError")
    
    def test_return_after_cleaning(self):
        lines = main.return_file_content('raw_data.txt')
        should_be_equal = [['State', 'Postal'],
                            ['Abbr.', 'FIPS'],
                            ['Code', 'State', 'Postal'],
                            ['Abbr.', 'FIPS'],
                            ['Code'],
                            ['Alabama', 'AL', '01', 'Nebraska', 'NE', '31']]
        for i in range(6):
            self.assertListEqual(main.return_after_cleaning(lines)[i], should_be_equal[i])

    def test_parser(self):
        data_to_be_parsed = ['Alabama', 'AL', '01']
        data_it_should_return = {'State': 'Alabama', 'Postal Abbr.': 'AL', 'FIPS Code': '01'}
        self.assertDictEqual(main.parser(data_to_be_parsed), data_it_should_return)

    
if __name__ == "main":
    unittest.main()

