import unittest

from validate_ip import validate_ip


class TestValidateIP(unittest.TestCase):

    def test_valid_ip(self):
        result = validate_ip("192.168.1.50")

        self.assertEqual(result, "192.168.1.50")
        self.assertIsInstance(result, str)

    def test_invalid_ip(self):
        result = validate_ip("999.999.999.999")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()