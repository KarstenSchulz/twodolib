import unittest

import twodolib


class TestShowUrls(unittest.TestCase):
    """Test the 4 urls to show several lists in 2Do App."""

    def test_showall_url(self):
        """Check, that showall url is correct."""
        expected_url = 'twodo://x-callback-url/showAll'
        self.assertEqual(twodolib.showall_url, expected_url)

    def test_showtoday_url(self):
        """Check, that showtoday url is correct."""
        expected_url = 'twodo://x-callback-url/showToday'
        self.assertEqual(twodolib.showtoday_url, expected_url)

    def test_showstarred_url(self):
        """Check, that showstarred url is correct."""
        expected_url = 'twodo://x-callback-url/showStarred'
        self.assertEqual(twodolib.showstarred_url, expected_url)

    def test_showscheduled_url(self):
        """Check, that showscheduled url is correct."""
        expected_url = 'twodo://x-callback-url/showScheduled'
        self.assertEqual(twodolib.showscheduled_url, expected_url)
