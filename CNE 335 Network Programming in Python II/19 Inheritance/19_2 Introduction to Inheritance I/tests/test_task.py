import unittest
from task import ServerClass, ServerWithOperatingSystemClass

class TestCase(unittest.TestCase):
    def test_create_server_with_operating_system_class_check_type(self):
        server = ServerClass("127.0.0.1", "localhost")
        self.assertIn("ServerClass", str(type(server)))

    def test_create_server_with_operating_system_class_get_server_class_information(self):
        server = ServerClass("127.0.0.1", "localhost")
        self.assertEqual("Name: localhost IP: 127.0.0.1", server.get_server_class_information())

    def test_server_with_operating_system_class_check_type(self):
        inherited_server = ServerWithOperatingSystemClass("127.0.0.1", "localhost", "Linux")
        self.assertIn("ServerWithOperatingSystemClass", str(type(inherited_server)))

    def test_server_with_operating_system_class_check_subclass(self):
        self.assertTrue(issubclass(ServerWithOperatingSystemClass, ServerClass))

    def test_server_with_operating_system_class_get_inherited_server_class_information(self):
        inherited_server = ServerWithOperatingSystemClass("127.0.0.1", "localhost", "Linux")
        self.assertIn("Name: localhost IP: 127.0.0.1", inherited_server.get_inherited_server_class_information())
        self.assertIn("Linux", inherited_server.get_inherited_server_class_information())
