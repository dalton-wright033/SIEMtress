import unittest

from process_event import process_event


class TestProcessEvent(unittest.TestCase):

    def test_valid_ip(self):
        event = {
            "ipv4": "192.168.1.50"
        }

        result = process_event(event)

        self.assertEqual(result["ipv4"], "192.168.1.50")
        self.assertEqual(result["ip_status"], "Valid")

    def test_invalid_ip(self):
        event = {
            "ipv4": "999.999.999.999"
        }

        result = process_event(event)

        self.assertIsNone(result["ipv4"])
        self.assertEqual(result["ip_status"], "Invalid")

    def test_missing_ip(self):
        event = {
            "ipv4": None
        }

        result = process_event(event)

        self.assertIsNone(result["ipv4"])
        self.assertEqual(result["ip_status"], "Missing")


if __name__ == "__main__":
    unittest.main()