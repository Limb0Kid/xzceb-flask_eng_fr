"""Import modules"""
import unittest
from translator import english_to_french
from translator import french_to_english


class TestMyModule(unittest.TestCase):
    """Unit testing class"""

    def test_english_to_french(self):
        """Test: Translation from English to French"""
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        """Test: Translation from from French to English"""
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
