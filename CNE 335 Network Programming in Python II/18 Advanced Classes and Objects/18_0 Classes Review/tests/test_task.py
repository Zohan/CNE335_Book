import unittest

from task import BareMetalServer

class TestCase(unittest.TestCase):
    def test_create_BareMetalServer_check_type(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        self.assertIn("BareMetalServer", str(type(bare_metal)))

    def test_create_BareMetalServer_check_cpu(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        if hasattr(bare_metal, "cpu"):
            self.assertEqual(bare_metal.cpu, "Intel Xeon")
        elif hasattr(bare_metal, "Cpu"):
            self.assertEqual(bare_metal.Cpu, "Intel Xeon")
        elif hasattr(bare_metal, "CPU"):
            self.assertEqual(bare_metal.CPU, "Intel Xeon")
        else:
            self.assertTrue(False, True, "Failed to find a CPU attribute!")

    def test_create_BareMetalServer_check_gpu(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        if hasattr(bare_metal, "gpu"):
            self.assertEqual(bare_metal.gpu, "NVIDIA GTX 3080")
        elif hasattr(bare_metal, "Gpu"):
            self.assertEqual(bare_metal.Gpu, "NVIDIA GTX 3080")
        elif hasattr(bare_metal, "GPU"):
            self.assertEqual(bare_metal.GPU, "NVIDIA GTX 3080")
        else:
            self.assertTrue(False, True, "Failed to find a GPU attribute!")

    def test_create_BareMetalServer_check_ram(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        if hasattr(bare_metal, "ram"):
            self.assertEqual(bare_metal.ram, "16GB 3000MHz")
        elif hasattr(bare_metal, "Ram"):
            self.assertEqual(bare_metal.Ram, "16GB 3000MHz")
        elif hasattr(bare_metal, "RAM"):
            self.assertEqual(bare_metal.RAM, "16GB 3000MHz")
        else:
            self.assertTrue(False, True, "Failed to find a RAM attribute!")

    def test_create_BareMetalServer_check_hdd(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        if hasattr(bare_metal, "hdd"):
            self.assertEqual(bare_metal.hdd, "16TB 7200RPM")
        elif hasattr(bare_metal, "Hdd"):
            self.assertEqual(bare_metal.Hdd, "16TB 7200RPM")
        elif hasattr(bare_metal, "HDD"):
            self.assertEqual(bare_metal.HDD, "16TB 7200RPM")
        else:
            self.assertTrue(False, True, "Failed to find a HDD attribute!")

    def test_create_BareMetalServer_get_system_info(self):
        bare_metal = BareMetalServer("Intel Xeon", "NVIDIA GTX 3080", "16GB 3000MHz", "16TB 7200RPM")
        system_info = bare_metal.get_system_info()
        self.assertIn("Intel Xeon", system_info)
        self.assertIn("NVIDIA GTX 3080", system_info)
        self.assertIn("16GB 3000MHz", system_info)
        self.assertIn("16TB 7200RPM", system_info)