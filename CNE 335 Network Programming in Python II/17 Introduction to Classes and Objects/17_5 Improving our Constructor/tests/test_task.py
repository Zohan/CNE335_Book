import unittest
from random import randint

from task import ServerClass

class TestCase(unittest.TestCase):
    def test_create_serverclass_type(self):
        server = ServerClass("127.0.0.1", "localhost")
        self.assertIn("ServerClass", str(type(server)))

    def test_server_name_exists(self):
        server = ServerClass("127.0.0.1", "localhost")
        self.assertTrue(hasattr(server, "server_name"))

    def test_set_server_name(self):
        server = ServerClass("127.0.0.1", "localhost")
        self.assertEqual("localhost", server.server_name)
        server.server_name = "random_server"
        self.assertEqual("random_server", server.server_name)