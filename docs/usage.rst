=====
Usage
=====

Using twodolib as a Python module
---------------------------------

To use twodolib and create a task::

    >>> from twodolib import TwoDoTask
    >>> my_task = TwoDoTask('Save the world.', priority=TwoDoTask.PRIO_HIGH)

    >>> my_task.url()
    u'twodo://x-callback-url/add?task=Save%20the%20world.&priority=3'


Using twodolib from the command line
------------------------------------

You can call ``task2do`` with a whole bunch of options. But it is easy to
add a standard task. Just enter::

    task2do -d 1 "Dinner at 8pm."

And you will get the URL to add a task, which is due tomorrow::

    twodo://x-callback-url/add?task=Dinner%20at%208pm.&due=1

Use the URL with Safari or Alfred or another launcher to actually create the
task. Or just provide the ``-e, --execute`` option, to actually create the
task in your 2Do App::

    task2do -e -d 1 "Dinner at 8pm."

You'll get help with the ``-h, --help`` option::

    task2do -h
    usage: task2do [-h] [-t {0,1,2}] [-l FOR_LIST] [-n NOTE] [-p {0,1,2,3}] [-s]
                   [--tags TAGS] [-d DUE] [--dueTime DUETIME] [--start START]
                   [--repeat {1,2,3,4}] [-i] [-v]
                   task

    Program to create tasks in 2Do. The default behavior is to print the
    generated URL to stdout. Please use the '-g' or '--go'' option, if you want to
    send the task directly to the 2DoApp.

    positional arguments:
      task                  Title of the task.

    optional arguments:
      -h, --help            show this help message and exit
      -t {0,1,2}, --type {0,1,2}
                            Type of task to create. Following options are
                            supported: 0 - Task (default), 1 - Project, 2 -
                            Checklist
      -l FOR_LIST, --list FOR_LIST
                            Name of an existing list in app, case-insensitive.
                            Default list or the currently visible list on screen
                            is selected if not used.
      -n NOTE, --note NOTE  Notes for the task
      -p {0,1,2,3}, --priority {0,1,2,3}
                            priority: 0 (none), 1 (low), 2 (medium), 3 (high)
      -s, --starred         Task is starred, if given.
      --tags TAGS           Comma separated list of tags to assign to the task
      -d DUE, --due DUE     Due Date. Supports two formats: YYYY-MM-DD - Sets on
                            the date on default due time (based on your settings,
                            unless due time is specified separately or
                            ignoreDefaults (-i) is given). OR: Any number - Number
                            of days from Today, starting from 0. e.g. 0 = Today, 1
                            = Tomorrow and so on)
      --dueTime DUETIME     Due Time. Supports 24h format HH:mm.
      --start START         Start Date and time. Supports the format: "YYYY-MM-DD
                            HH:MM" - Sets the start date on the date and time
                            specified - OR - Any number - Number of days from
                            Today, starting from 0. e.g. 0 = Today, 1 = Tomorrow
                            and so on)
      --repeat {1,2,3,4}    Repeat task: 1 (daily), 2 (weekly), 3 (bi-weekly), 4
                            (monthly))
      -i, --ignoreDefaults  If not set (default), apply any default due date /
                            time settings in app. Ignore default dates / times, if
                            given.
      -v, --version         show program's version number and exit


Examples
--------

Add a task due Tomorrow::

    task2do -d 1 "Dinner at 8pm."

Add a task with high priority::

    task2do -p 3 "High priority task."
    task2do --priority 3 "High priority task."

Add a task due today and repeated weekly::

    task2do "change clothes" -d 0 --repeat 2

Add a task due at 6pm today::

    task2do "Watch EX_MACHINA" --due 0 --dueTime 18:00

Add a task due tomorrow, with tags, which is also starred and repeated monthly::

    task2do "Monthly subscription." --tags bill,payment -s --due 1 --repeat 4

