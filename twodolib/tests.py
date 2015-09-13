"""Unittests for twodolib."""

import unittest
import urllib

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


class TestGetSimpleAddUrl(unittest.TestCase):

    """Test url for adding tasks to 2Do App."""

    def test_add_task_with_title_url(self):
        """Test adding a task only with a title."""
        task_title = 'Test title of the task.'
        quoted_title = urllib.quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        self.assertEqual(twodolib.get_add_url(task_title), expected_url)


@unittest.skip
class TestTwoDoTaskClass(unittest.TestCase):

    """Test the representation of a 2Do task."""

    def test_simple_task_with_title_only(self):
        """Create a simple task only by title."""
        title = 'A simple task by title'
        task = twodolib.TwoDoTask(title)
        self.assertEqual(task.task, title)

    def test_default_values_of_simple_task(self):
        """Create a task by title and check the other default values."""
        task = twodolib.TwoDoTask('Save the world.')
        self.assertEqual(task.task, 'Save the world.')
        self.assertEqual(task.type, twodolib.TwoDoTask.TASK)
        self.assertIsNone(task.for_list)


if __name__ == '__main__':
    unittest.main()
