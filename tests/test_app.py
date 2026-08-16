import os
import subprocess
import sys
import unittest


class ReleaseBoardTests(unittest.TestCase):
    def run_board(self, *args, **env):
        return subprocess.run([sys.executable, "-m", "release_board", *args], text=True, capture_output=True, env={**os.environ, **env})

    def test_human_board_shows_blocked_item(self):
        result = self.run_board()
        self.assertEqual(result.returncode, 0)
        self.assertIn("[BLOCKED] ! Prepare migration", result.stdout)

    def test_json_is_inspectable(self):
        result = self.run_board("--json")
        self.assertEqual(result.returncode, 0)
        self.assertIn('"RB-104"', result.stdout)

    def test_missing_data_is_actionable(self):
        result = self.run_board("--doctor", RELEASE_DATA="missing-items.json")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Check RELEASE_DATA", result.stderr)
