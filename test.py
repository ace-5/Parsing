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

    
if __name__ == "main":
    unittest.main()

