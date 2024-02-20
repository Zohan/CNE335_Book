import unittest
from random import randint

from task import ServerClass, dhcp_service

class TestCase(unittest.TestCase):
    def test_create_serverclass_type(self):
        server = ServerClass()
        self.assertIn("ServerClass", str(type(server)))

    def test_dhcp_ip_not_equal_to_base(self):
        server = ServerClass()
        base_ip = server.ip
        server.request_dhcp_ip()
        self.assertNotEqual(base_ip, server.ip)

    def test_ip_keep_first_octet(self):
        server = ServerClass()
        base_ip = server.ip
        base_ip_split = base_ip.split(".")
        base_ip_first_part = base_ip_split[0]
        server.request_dhcp_ip()
        new_ip_split = server.ip.split(".")
        new_ip_first_part = new_ip_split[0]
        self.assertEqual(base_ip_first_part, new_ip_first_part)

    def test_dhcp_issues_different_ips(self):
        server_one = ServerClass()
        server_one.request_dhcp_ip()
        server_two = ServerClass()
        server_two.request_dhcp_ip()
        server_three = ServerClass()
        server_three.request_dhcp_ip()
        self.assertNotEqual(server_one.ip, server_two.ip)
        self.assertNotEqual(server_two.ip, server_three.ip)
        self.assertNotEqual(server_one.ip, server_three.ip)