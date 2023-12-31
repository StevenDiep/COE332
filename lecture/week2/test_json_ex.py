import unittest
from json_ex import check_char_count
from json_ex import check_char_type
from json_ex import check_char_match

class TestJsonEx(unittest.TestCase):

    def test_check_char_count(self):
        self.assertEqual(check_char_count('AA'), 'AA count passes')
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
        self.assertRaises(AssertionError, check_char_count, 1)
        self.assertRaises(AssertionError, check_char_count, True)
        self.assertRaises(AssertionError, check_char_count, ['AA', 'BB'])

    def test_check_char_type(self):
         self.assertEqual(check_char_type('AA'), 'AA type passes')
         self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
         self.assertEqual(check_char_type('aa'), 'aa type FAILS')
         self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
         self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
         self.assertRaises(AttributeError, check_char_type, 1)
         self.assertRaises(AttributeError, check_char_type, True)
         self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])

    def test_check_char_match(self):
        self.assertEqual(check_char_match('Texas', 'TX'), 'Texas match passes')
        self.assertEqual(check_char_match('Texas', 'AZ'), 'Texas match FAILS')
        self.assertRaises(AssertionError, check_char_match, '1', ['1', 2])
        self.assertRaises(AssertionError, check_char_match, 'True', True)
        self.assertRaises(AssertionError, check_char_match, '1', 1)

if __name__ == '__main__':
    unittest.main()
