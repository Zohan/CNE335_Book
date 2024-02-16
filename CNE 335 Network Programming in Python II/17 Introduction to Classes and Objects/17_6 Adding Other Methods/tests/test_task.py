import unittest
from random import randint

from task import ServerClass

class TestCase(unittest.TestCase):
    def test_create_serverclass_type(self):
        random_ip = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip += "." + str(randint(1, 254))
        server = ServerClass(random_ip)
        self.assertIn("ServerClass", str(type(server)))

    def test_get_server_ip_exists(self):
        random_ip = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip += "." + str(randint(1, 254))
        server = ServerClass(random_ip)
        self.assertTrue(hasattr(server, "get_server_ip"))

    def test_get_server_ip_change_ip(self):
        random_ip = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip += "." + str(randint(1, 254))
        server = ServerClass(random_ip)
        self.assertEquals(random_ip, server.get_server_ip())
        random_ip_two = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip_two += "." + str(randint(1, 254))
        server.server_ip = random_ip_two
        self.assertEquals(random_ip_two, server.get_server_ip())

    def test_get_server_ip_two_objects(self):
        random_ip_one = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip_one += "." + str(randint(1, 254))
        random_ip_two = str(randint(2, 254))  # Start at 2 to make 127.0.0.1 impossible
        for i in range(0, 3):
            random_ip_two += "." + str(randint(1, 254))
        server_one = ServerClass(random_ip_one)
        self.assertEquals(random_ip_one, server_one.get_server_ip())
        server_two = ServerClass(random_ip_two)
        self.assertEquals(random_ip_two, server_two.get_server_ip())