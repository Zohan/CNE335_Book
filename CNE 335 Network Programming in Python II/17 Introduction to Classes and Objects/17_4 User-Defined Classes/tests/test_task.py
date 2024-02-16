import unittest
from random import randint

from task import ServerClass

class TestCase(unittest.TestCase):
    def test_create_serverclass_type(self):
        server = ServerClass()
        self.assertIn("ServerClass", str(type(server)))

    def test_server_name_exists(self):
        server = ServerClass()
        self.assertTrue(hasattr(server, "server_name"))

    def test_get_server_name(self):
        server = ServerClass()
        self.assertIsNotNone(server.get_server_name())
        self.assertNotEqual(self, "<class 'method'>", str(type(server.server_name)))

    def test_set_server_name(self):
        server = ServerClass()
        random_server = "localhost_" + str(randint(0,254))
        server.server_name = random_server
        self.assertEquals(random_server, server.server_name)
        self.assertEquals(random_server, server.get_server_name())