import unittest

from thresholds import get_disk_status, get_memory_status


class TestDiskStatus(unittest.TestCase):
    def test_normal_usage(self):
        self.assertEqual(get_disk_status(50), "NORMAL")

    def test_warning_boundary(self):
        self.assertEqual(get_disk_status(80), "WARNING")

    def test_critical_boundary(self):
        self.assertEqual(get_disk_status(90), "CRITICAL")

    def test_just_below_warning(self):
        self.assertEqual(get_disk_status(79), "NORMAL")

    def test_just_below_critical(self):
        self.assertEqual(get_disk_status(89), "WARNING")


class TestMemoryStatus(unittest.TestCase):
    def test_normal_usage(self):
        self.assertEqual(get_memory_status(50), "NORMAL")

    def test_warning_boundary(self):
        self.assertEqual(get_memory_status(80), "WARNING")

    def test_critical_boundary(self):
        self.assertEqual(get_memory_status(90), "CRITICAL")

    def test_just_below_warning(self):
        self.assertEqual(get_memory_status(79), "NORMAL")

    def test_just_below_critical(self):
        self.assertEqual(get_memory_status(89), "WARNING")


if __name__ == "__main__":
    unittest.main()
