# -*- coding: utf-8 -*-

"""Tests for `twodolib` module."""
import unittest
import sys

import twodolib
from twodolib import TwoDoTask

PY3 = sys.version_info > (3,)
if PY3:
    from urllib.parse import quote
else:
    from urllib import quote


class TestShowUrls(unittest.TestCase):

    """Test the 4 urls to show several lists in 2Do App."""

    def test_showall_url(self):
        """URL showall is correct."""
        expected_url = 'twodo://x-callback-url/showAll'
        self.assertEqual(twodolib.showall_url, expected_url)

    def test_showtoday_url(self):
        """URL showtoday is correct."""
        expected_url = 'twodo://x-callback-url/showToday'
        self.assertEqual(twodolib.showtoday_url, expected_url)

    def test_showstarred_url(self):
        """URL showstarred is correct."""
        expected_url = 'twodo://x-callback-url/showStarred'
        self.assertEqual(twodolib.showstarred_url, expected_url)

    def test_showscheduled_url(self):
        """URL showscheduled is correct."""
        expected_url = 'twodo://x-callback-url/showScheduled'
        self.assertEqual(twodolib.showscheduled_url, expected_url)


class TestGetSimpleAddUrl(unittest.TestCase):

    """Test url for adding tasks to 2Do App."""

    def test_add_task_with_title_url(self):
        """Test adding a task only with a title."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        self.assertEqual(twodolib.get_add_url(task_title), expected_url)


class TestTwoDoTaskClass(unittest.TestCase):

    """Test the representation of a 2Do task."""

    def test_simple_task_with_title_only(self):
        """Create a simple task only by title."""
        title = 'A simple task by title'
        task = twodolib.TwoDoTask(title)
        self.assertEqual(task.task, title)

    def test_task_with_title_length_of_zero_raises_valueerror(self):
        """Create a simple task only by title."""
        title = ''
        self.assertRaises(ValueError, twodolib.TwoDoTask, title)

    def test_default_values_of_simple_task(self):
        """Create a task by title and check the presence of attributes."""
        task = twodolib.TwoDoTask('Save the world.')
        self.assertEqual(task.task, 'Save the world.')
        self.assertEqual(task.type, twodolib.TwoDoTask.TASK_TYPE)
        self.assertIsNone(task.for_list)
        self.assertIsNone(task.forParentTask)
        self.assertIsNone(task.note)
        self.assertEqual(task.priority, '0')
        self.assertEqual(task.starred, '0')
        self.assertIsNone(task.tags)
        self.assertIsNone(task.due)
        self.assertIsNone(task.dueTime)
        self.assertIsNone(task.start)
        self.assertIsNone(task.repeat)
        self.assertIsNone(task.action)
        self.assertEqual(task.ignoreDefaults, '0')

    def test_simple_task_url_is_correct(self):
        """The URL for a simple task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        task = TwoDoTask(task_title)
        self.assertEqual(task.url(), expected_url)

    def test_project_task_url_is_correct(self):
        """The URL for a project task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&type=1'
        task = TwoDoTask(task_title, type='1')
        self.assertEqual(task.url(), expected_url)

    def test_task_for_a_list_url_is_correct(self):
        """The URL for a task for a list is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        quoted_list = quote('urgent errands')
        expected_url += '&for_list={}'.format(quoted_list)
        task = TwoDoTask(task_title, for_list='urgent errands')
        self.assertEqual(task.url(), expected_url)
