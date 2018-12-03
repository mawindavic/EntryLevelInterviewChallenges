import unittest
from additive_sequence import has_additive_sequence


class TestAdditiveSequence(unittest.TestCase):
    """Tests for checking if a string has active sequence"""

    def test_non_digit_string(self):
        """Test a string that is not a digit
        """
        arg1 = "6,6,12,18,30"
        actual = has_additive_sequence(arg1)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

        arg2 = "6,6,12,19,30"
        actual = has_additive_sequence(arg2)
        expected = False
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

    def test_digit_string(self):
        arg1 = "1235"
        actual = has_additive_sequence(arg1)
        expected = True
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

        arg2 = "12345"
        actual = has_additive_sequence(arg2)
        expected = False
        message = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, message)

if __name__ == "__main__":
    unittest.main(exit=False)
