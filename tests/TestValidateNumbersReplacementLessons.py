import unittest
from modules.parser import validate_numbers_replacement_lessons


class TestValidateNumbersReplacementLessons(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(validate_numbers_replacement_lessons('1'), [1])

    def test_multiple_numbers(self):
        self.assertEqual(validate_numbers_replacement_lessons('1,2,3'), [1, 2, 3])

    def test_range_of_numbers(self):
        self.assertEqual(validate_numbers_replacement_lessons('2-4'), [2, 3, 4])

    def test_float_number_mapping(self):
        self.assertEqual(validate_numbers_replacement_lessons('9.10'), [0])
        self.assertEqual(validate_numbers_replacement_lessons('10.50'), [1])
        self.assertEqual(validate_numbers_replacement_lessons('12.30'), [2])
        self.assertEqual(validate_numbers_replacement_lessons('14.50'), [3])
        self.assertEqual(validate_numbers_replacement_lessons('16.35'), [4])
        self.assertEqual(validate_numbers_replacement_lessons('18.35'), [5])
        self.assertEqual(validate_numbers_replacement_lessons('20.00'), [6])

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            validate_numbers_replacement_lessons('a')
        with self.assertRaises(Exception):
            validate_numbers_replacement_lessons('1,a,3')
        with self.assertRaises(Exception):
            validate_numbers_replacement_lessons('1-a')
        with self.assertRaises(Exception):
            validate_numbers_replacement_lessons('1-3-5')
        with self.assertRaises(Exception):
            validate_numbers_replacement_lessons('1,2,3,7')


if __name__ == '__main__':
    unittest.main()