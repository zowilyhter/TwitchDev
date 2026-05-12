# test_twitchdev.py
"""
Tests for TwitchDev module.
"""

import unittest
from twitchdev import TwitchDev

class TestTwitchDev(unittest.TestCase):
    """Test cases for TwitchDev class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TwitchDev()
        self.assertIsInstance(instance, TwitchDev)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TwitchDev()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
