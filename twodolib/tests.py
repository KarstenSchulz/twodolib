import unittest

import twodolib


class TestShowUrls(unittest.TestCase):
    """Test the 4 urls to show several lists in 2Do App."""

    def test_showall_url(self):
        showall_url = 'twodo://x-callback-url/showAll'
        self.assertEqual(twodolib.showall_url, showall_url)

    def test_showtoday_url(self):
        showtoday_url = 'twodo://x-callback-url/showToday'
        self.assertEqual(twodolib.showtoday_url, showtoday_url)

    def test_showstarred_url(self):
        showstarred_url = 'twodo://x-callback-url/showStarred'
        self.assertEqual(twodolib.showstarred_url, showstarred_url)

    def test_showscheduled_url(self):
        showscheduled_url = 'twodo://x-callback-url/showScheduled'
        self.assertEqual(twodolib.showscheduled_url, showscheduled_url)
