"""Command line interface to add tasks to 2Doapp."""

import argparse

examples = '''
Examples
========

Add a task due Tomorrow:
task2do -d 1 "Dinner at 8pm."

Add a task with high priority:
task2do -p 3 "High priority task."
- or -
task2do --priority 3 "High priority task."

Add a weekly repeating task:
task2do "change clothes" --repeat 2

Add a task due at 6pm today
task2do "Watch EX_MACHINA" --dueTime 18:00

Add a task with tags, which is also starred and repeated monthly
task2do "Monthly subscription." --tags bill,payment -s --repeat 4
'''


def main():
    """Parse command line arguments and create TwoDoTask object."""
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog='task2do',
        description='''Program to create tasks in 2Do.''',
        epilog=examples
    )
    p.add_argument('task', help='Title of the task.')
    p.add_argument('-t', '--type', choices=[0, 1, 2],
                   help='Type of task to create. Following options are '
                        'supported: 0 - Task (default), 1 - Project, '
                        '2 - Checklist',
                   default=0)
    p.add_argument('-l', '--list', metavar='FOR_LIST',
                   help='Name of an existing list in app, case-insensitive. '
                        'Default list or the currently visible list on screen '
                        'is selected if not used.',
                   default=None)
    p.add_argument('-n', '--note', help='Notes for the task',
                   default=None)
    p.add_argument('-p', '--priority', choices=[0, 1, 2, 3],
                   help='priority: 0 (none), 1 (low), 2 (medium), 3 (high)',
                   default=0)
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
    p.add_argument('--repeat', default=None, choices=[1, 2, 3, 4],
                   help='Repeat task: 1 (daily), 2 (weekly), 3 (bi-weekly), '
                        '4 (monthly))')
    p.add_argument('-i', '--ignoreDefaults', action='store_true',
                   default=False,
                   help='If not set (default), apply any default due date / '
                        'time settings in app. Ignore default dates / times, '
                        'if given.')
    p.parse_args()
    # TODO: create TwoDoTask


if __name__ == '__main__':
    main()
