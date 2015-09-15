# -*- coding: utf-8 -*-

"""Tests for `twodolib.cli` module."""

import unittest
import sys
from twodolib import TwoDoTask
from twodolib import cli


class TestCliParseArguments(unittest.TestCase):

    """Test the command line interface and argument parsing."""

    def test_default_task_is_task_type(self):
        """Default task type should be 'task'."""
        parsed = cli.parse_arguments(['TestTask'])
        self.assertEqual(parsed.type, TwoDoTask.TASK_TYPE)

    def test_set_task_type_project(self):
        """A task can be a 'project' type: -t 1."""
        args = "TestTask -t 1".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.type, TwoDoTask.PROJECT_TYPE)

    def test_set_task_type_project_long_option(self):
        """A task can be a 'project' type: --type 1."""
        args = "TestTask --type 1".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.type, TwoDoTask.PROJECT_TYPE)

    def test_set_task_type_checklist(self):
        """A task can be a 'checklist' type: -t 2."""
        args = "TestTask -t 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.type, TwoDoTask.CHECKLIST_TYPE)

    def test_set_task_type_checklist_long_option(self):
        """A task can be a 'checklist' type: --type 2."""
        args = "TestTask --type 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.type, TwoDoTask.CHECKLIST_TYPE)

    def test_set_list_name(self):
        """A task can belong to a list: -l listname."""
        args = "TestTask -l business".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.list, 'business')

    def test_set_list_name_long_option(self):
        """A task can belong to a list: --list listname."""
        args = "TestTask --list business".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.list, 'business')

    def test_set_note_of_task(self):
        """A task can have a note: -n "some notes to the task ..."."""
        args = [
            'TestTask',
            '-n',
            'This is a note for the task.'
        ]
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.note, 'This is a note for the task.')

    def test_set_note_of_task_long_option(self):
        """A task can have a note: --note "some notes to the task ..."."""
        args = [
            'TestTask',
            '--note',
            'This is a note for the task.'
        ]
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.note, 'This is a note for the task.')

    def test_set_priority(self):
        """Priority of a task can be set: -p 2."""
        args = "TestTask -p 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.priority, '2')

    def test_set_priority_long_option(self):
        """Priority of a task can be set: --priority 2."""
        args = "TestTask --priority 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.priority, '2')

    def test_not_starring_task_is_default(self):
        """The default task is not starred."""
        args = ["TestTask"]
        parsed = cli.parse_arguments(args)
        self.assertFalse(parsed.starred)

    def test_starr_task(self):
        """Starr a task with: -s."""
        args = "TestTask -s".split()
        parsed = cli.parse_arguments(args)
        self.assertTrue(parsed.starred)

    def test_starr_task_long_option(self):
        """Starr a task with: --starred."""
        args = "TestTask --starred".split()
        parsed = cli.parse_arguments(args)
        self.assertTrue(parsed.starred)

    def test_set_tags_in_task(self):
        """A Task can have tags."""
        args = "TestTask --tags business,customer,important".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.tags, "business,customer,important")

    def test_set_due_date_isoformat(self):
        """Set the tasks due date: -d YYYY-MM-DD."""
        args = "TestTask -d 2015-09-10".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.due, "2015-09-10")

    def test_set_due_date_isoformat_long_option(self):
        """Set the tasks due date: --due YYYY-MM-DD."""
        args = "TestTask --due 2015-09-10".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.due, "2015-09-10")

    def test_set_due_date_n_format(self):
        """Set the tasks due date: -d 2."""
        args = "TestTask -d 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.due, "2")

    def test_set_due_date_n_format_long_option(self):
        """Set the tasks due date: --due 14."""
        args = "TestTask --due 14".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.due, "14")

    def test_set_duetime(self):
        """Set the tasks due time: --dueTime '2015-09-10 12:00'."""
        args = "TestTask --dueTime".split()
        args.append('2015-09-10 12:00')
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.dueTime, "2015-09-10 12:00")

    def test_set_start_isoformat(self):
        """Set the tasks start time: --start '2015-09-10 12:00'."""
        args = "TestTask --start".split()
        args.append('2015-09-10 12:00')
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.start, "2015-09-10 12:00")

    def test_set_start_n_format(self):
        """Set the tasks start time: --start 7."""
        args = "TestTask --start 7".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.start, "7")

    def test_repeat_task(self):
        """Create a repeating task: --repeat 2."""
        args = "TestTask --repeat 2".split()
        parsed = cli.parse_arguments(args)
        self.assertEqual(parsed.repeat, "2")

    def test_ignoredefaults_default_to_false(self):
        """Do not ignore defaults."""
        parsed = cli.parse_arguments(['TestTask'])
        self.assertFalse(parsed.ignoreDefaults)

    def test_set_ignoredefaults(self):
        """Ignore defaults: -i."""
        args = "TestTask -i".split()
        parsed = cli.parse_arguments(args)
        self.assertTrue(parsed.ignoreDefaults)

    def test_set_ignoredefaults_long_option(self):
        """Ignore defaults: --ignoerDefaults."""
        args = "TestTask --ignoreDefaults".split()
        parsed = cli.parse_arguments(args)
        self.assertTrue(parsed.ignoreDefaults)

    def test_missing_args_raise_system_exit(self):
        """Raise SystemExit, if args are missing."""
        sys.argv = []
        with self.assertRaises(SystemExit):
            cli.main()
