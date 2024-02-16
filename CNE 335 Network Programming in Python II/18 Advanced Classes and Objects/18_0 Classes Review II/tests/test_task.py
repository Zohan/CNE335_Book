import unittest

from task import NetworkCardClass, NetworkServerClass

class TestCase(unittest.TestCase):
    def test_create_networkcardclass_check_type(self):
        network_card = NetworkCardClass("127.0.0.1", "Broadcom")
        self.assertIn("NetworkCardClass", str(type(network_card)))

    def test_create_networkcardclass_check_attributes(self):
        network_card = NetworkCardClass("127.0.0.1", "Broadcom")
        self.assertEqual(network_card.ip_address, "127.0.0.1")
        self.assertEqual(network_card.model_name, "Broadcom")

    def test_create_networkserverclass_check_type(self):
        server = NetworkServerClass("AWS Linux", NetworkCardClass("127.0.0.1", "Broadcom"))
        self.assertIn("ServerClass", str(type(server)))

    def test_create_networkserverclass_check_attributes(self):
        server = NetworkServerClass("AWS Linux", NetworkCardClass("127.0.0.1", "Broadcom"))
        self.assertIn("ServerClass", str(type(server)))
        self.assertEqual(server.server_name, "AWS Linux")
        self.assertEqual(server.network_card.ip_address, "127.0.0.1")
        self.assertEqual(server.network_card.model_name, "Broadcom")

    def test_server_details(self):
        server = NetworkServerClass("AWS Linux V2", NetworkCardClass("36.8.12.1", "Intel"))
        server_details = server.get_server_details()
        self.assertIn("AWS Linux", server_details)
        self.assertIn("36.8.12.1", server_details)
        self.assertIn("Intel", server_details)