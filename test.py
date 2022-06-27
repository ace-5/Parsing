import unittest
import main

class TestParserProgram(unittest.TestCase):
    def test_get_file(self):
        self.assertIsInstance(main.get_data_lines('raw_data.txt'), list, msg= "Returned Obejct is not list")

    def test_remove_whitespace(self):
        mystring = ["Hello From\n", "the other side\n"]
        self.assertIsInstance(main.remove_whitespace(mystring), list, msg="Pass list which contains string as argument")
        
    def test_to_make_string_individual(self):
        myList = ["Hello from", "the other side"]
        expected = ["Hello", "from", "the", "other", "side"]
        self.assertEqual(main.make_each_word_listItem(myList), expected, msg="Function doesnot returns expected lsit")
    
if __name__ == "main":
    unittest.main()

