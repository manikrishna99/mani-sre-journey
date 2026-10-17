import subprocess
import unittest
from unittest.mock import patch

from health_checker import check_uptime


class TestUptimeCheck(unittest.TestCase):
    @patch("health_checker.subprocess.run")
    def test_uptime_returns_output(self, mock_run):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["uptime"],
            returncode=0,
            stdout="up 2 hours\n",
            stderr="",
        )

        self.assertEqual(check_uptime(), "up 2 hours")

    @patch("health_checker.subprocess.run", side_effect=FileNotFoundError)
    def test_missing_uptime_command(self, mock_run):
        with self.assertRaises(FileNotFoundError):
            check_uptime()

    @patch(
        "health_checker.subprocess.run",
        side_effect=subprocess.CalledProcessError(1, ["uptime"]),
    )
    def test_uptime_command_failure(self, mock_run):
        with self.assertRaises(subprocess.CalledProcessError):
            check_uptime()


if __name__ == "__main__":
    unittest.main()
