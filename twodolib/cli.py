# coding=utf-8
"""Command line interface to add tasks to 2Doapp."""

from __future__ import print_function, unicode_literals
import argparse
import sys
import webbrowser

import twodolib
from . urlhelper import TwoDoTask

usage_description = """\
Program to create tasks in 2Do. The default behavior is to print the
generated URL to stdout. Please use the '-g' or '--go'' option, if you want to
send the task directly to the 2DoApp.

Examples
========

Add a task due Tomorrow:
task2do -d 1 "Dinner at 8pm."

Add a task with high priority:
task2do -p 3 "High priority task."
- or -
task2do --priority 3 "High priority task."

Add a task due today and repeated weekly:
task2do "change clothes" -d 0 --repeat 2

Add a task due at 6pm today
task2do "Watch EX_MACHINA" --due 0 --dueTime 18:00

Add a task due tomorrow, with tags, which is also starred and repeated monthly
task2do "Monthly subscription." --tags bill,payment -s --due 1 --repeat 4

"""


def parse_arguments(args):
    """Return Namespace with parsed command line arguments."""
    version = '%(prog)s {}'.format(twodolib.__version__)
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog='task2do',
        description=usage_description,
    )
    p.add_argument('task', help='Title of the task.')
    p.add_argument('-t', '--type', choices=['0', '1', '2'], dest='task_type',
                   help='Type of task to create. Following options are '
                        'supported: 0 - Task (default), 1 - Project, '
                        '2 - Checklist', default='0')
    p.add_argument('-l', '--list', metavar='FOR_LIST', dest='for_list',
                   help='Name of an existing list in app, case-insensitive. '
                        'Default list or the currently visible list on screen '
                        'is selected if not used.',
                   default=None)
    p.add_argument('-n', '--note', help='Notes for the task',
                   default=None)
    p.add_argument('-p', '--priority', choices=['0', '1', '2', '3'],
                   help='priority: 0 (none), 1 (low), 2 (medium), 3 (high)',
                   default='0')
    p.add_argument('-s', '--starred', help='Task is starred, if given.',
                   action='store_true', default=False)
    p.add_argument('--tags', default=None,
                   help='Comma separated list of tags to assign to the task')
    p.add_argument('-d', '--due', default=None,
                   help='Due Date. Supports two formats: YYYY-MM-DD - Sets on '
                        'the date on default due time (based on your '
                        'settings, unless due time is specified separately or '
                        'ignoreDefaults (-i) is given). OR: Any number - '
                        'Number of days from Today, starting from 0. e.g. 0 = '
                        'Today, 1 = Tomorrow and so on)')
    p.add_argument('--dueTime', default=None,
                   help='Due Time. Supports 24h format HH:mm.')
    p.add_argument('--start', default=None,
                   help='Start Date and time. Supports the format: '
                        '"YYYY-MM-DD HH:MM" - Sets the start date on the date '
                        'and time specified - OR - Any number - Number of '
                        'days from Today, starting from 0. e.g. 0 = Today, '
                        '1 = Tomorrow and so on)')
    p.add_argument('--repeat', default=None, choices=['1', '2', '3', '4'],
                   help='Repeat task: 1 (daily), 2 (weekly), 3 (bi-weekly), '
                        '4 (monthly))')
    p.add_argument('-i', '--ignoreDefaults', action='store_true',
                   default=False,
                   help='If not set (default), apply any default due date / '
                        'time settings in app. Ignore default dates / times, '
                        'if given.')
    p.add_argument('-e', '--execute', action='store_true',
                   help='Actually open the URL and add the task instead of'
                        'showing the URL on stdout.')
    p.add_argument('-v', '--version', action='version', version=version)
    return p.parse_args(args)


def main(arguments=None):
    """Create a task in 2DoApp."""
    if arguments is None:
        arguments = sys.argv[1:]
    args = parse_arguments(arguments)
    t = TwoDoTask(**vars(args))
    if args.execute:
        webbrowser.open(t.url())
    else:
        print(t.url())


if __name__ == '__main__':  # pragma: no cover
    main(sys.argv[1:])
