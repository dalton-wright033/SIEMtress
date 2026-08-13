import unittest

from extract_event import extract_event


class TestExtractEvent(unittest.TestCase):

    def test_extract_complete_event(self):
        line = (
            "Aug 13 14:32:10 server "
            "sshd: Failed password for invalid user admin "
            "from 192.168.1.50 port 22"
        )

        result = extract_event(line)

        expected = {
            "month": "Aug",
            "day": "13",
            "time": "14:32:10",
            "host": "server",
            "ipv4": "192.168.1.50",
            "port": "22",
            "username": "admin"
        }

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()