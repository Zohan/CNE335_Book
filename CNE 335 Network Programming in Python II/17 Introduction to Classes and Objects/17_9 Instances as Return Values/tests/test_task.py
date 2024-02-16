import unittest
from random import randint

from task import ServerClass, biggest_server_object_sum

class TestCase(unittest.TestCase):
    def test_create_serverclass_type(self):
        server = ServerClass("0.0.0.0")
        self.assertIn("ServerClass", str(type(server)))

    def test_biggest_ip_sum_zero_and_one(self):
        ip_zero = ServerClass("0.0.0.0")
        ip_one = ServerClass("0.0.0.1")
        self.assertEquals(biggest_server_object_sum(ip_zero, ip_one), ip_one)

    def test_biggest_ip_sum_localhost_and_dhcp(self):
        ip_localhost = ServerClass("127.0.0.1")
        ip_dhcp = ServerClass("192.168.0.1")
        self.assertEquals(biggest_server_object_sum(ip_localhost, ip_dhcp), ip_dhcp)

    def test_random_ip(self):
        random_ip_octet = randint(2, 250)
        random_ip = str(random_ip_octet)  # Start at 2 to make 127.0.0.1 impossible
        random_bigger_ip = str(random_ip_octet + 2)
        bigger_ip_total = random_ip_octet+2
        for i in range(0, 3):
            random_ip_octet = randint(2, 250)
            random_ip += "." + str(random_ip_octet)
            random_bigger_ip += "." + str(random_ip_octet+2)
            bigger_ip_total += random_ip_octet+2
        ip_base = ServerClass(random_ip)
        ip_bigger = ServerClass(random_bigger_ip)
        self.assertEquals(biggest_server_object_sum(ip_base, ip_bigger), ip_bigger)