import unittest

import twodolib


class TestShowUrls(unittest.TestCase):
    """Test the 4 urls to show several lists in 2Do App."""

    def test_showall_url(self):
        showall_url = 'twodo://x-callback-url/showAll'
        self.assertEqual(twodolib.showall_url, showall_url)
