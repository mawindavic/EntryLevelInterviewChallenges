import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """Test for whether a stings are palindromes or not
    """

    def test_non_empty_string(self):
        """Test for palindrome in non empty string"""
        
        store = []
        expected_store = ["madam", "Level", "Brian"]
        arg1 = "madam"
        actual = is_palindrome(arg1, store)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

        arg2 = "Level"
        actual = is_palindrome(arg2, store)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

        arg3 = "Brian"
        actual = is_palindrome(arg3, store)
        expected = False
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected)
        message = "Expected {} as record, but returned {}".format(
            expected_store, store)
        self.assertEqual(store, expected_store, message)

    def test_for_empty_string(self):
        """Test for an empty string
        """

        store = []
        arg1 = ""
        actual = is_palindrome(arg1, store)
        expected = True
        expected_store = [""]
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)
        message = "Expected {} as record, but returned {}".format(
            expected_store, store)
        self.assertEqual(store, expected_store, message)

    def test_for_asingle_character(self):
        """Test for a single character string
        """

        store = []
        expected_store = ["a"]
        arg1 = "a"
        actual = is_palindrome(arg1, store)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)
        message = "Expected {} as record, but returned {}".format(
            expected_store, store)
        self.assertEqual(store, expected_store, message)

    def test_white_spaces(self):
        """Test for strings with white spaces
        """

        store = []
        expected_store = ["nurses run"]
        arg1 = "nurses run"
        actual = is_palindrome(arg1, store)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)
        message = "Expected {} as record, but returned {}".format(
            expected_store, store)
        self.assertEqual(store, expected_store, message)

    def test_last_five_records(self):
        """Test for keeping of record of last five entries
        """
        
        store = ["a", "b", "Hello", "try", "level"]
        expected_store = ["b", "Hello", "try", "level", "bayesian nets"]
        arg1 = "bayesian nets"
        is_palindrome(arg1, store)
        message = "Expected {} as record, but returned {}".format(
            expected_store, store)
        self.assertEqual(store, expected_store, message)


if __name__ == '__main__':
    unittest.main(exit=False)
