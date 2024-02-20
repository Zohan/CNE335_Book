import unittest
from random import randint

from task import is_ip_localhost, who_assigned_ip

class TestCase(unittest.TestCase):
    def test_is_ip_localhost_bool_return_type(self):
        self.assertEqual(type(is_ip_localhost("127.0.0.1")), bool)

    def test_local_ip(self):
        self.assertEqual(is_ip_localhost("127.0.0.1"), True)

    def test_random_not_local_ip(self):
        random_ip = str(randint(2,254)) # Start at 2 to make 127.0.0.1 impossible
        for i in range(0,3):
            random_ip += "."+ str(randint(1,254))
        self.assertEqual(is_ip_localhost(random_ip), False)

    def test_who_assigned_ip_string_return_type(self):
        self.assertEqual(type(who_assigned_ip("127.0.0.1")), str)

    def test_who_assigned_ip_localhost(self):
        self.assertEqual(who_assigned_ip("127.0.0.1"), "Localhost")

    def test_who_assigned_ip_dhcp(self):
        self.assertEqual(who_assigned_ip("192.168.0.1"), "DHCP")

    def test_who_assigned_ip_dhcp(self):
        random_ip = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        self.assertEqual(who_assigned_ip(f"192.168.0.{random_ip}"), "DHCP")

    def test_who_assigned_ip_unknown(self):
        self.assertEqual(who_assigned_ip("10.0.0.1"), "Unknown")