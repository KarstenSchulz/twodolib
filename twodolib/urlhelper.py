"""
Module to generate URLs to manage tasks, checlists and projects in 2DoApp.

see http://www.2doapp.com

"""
from __future__ import unicode_literals
import sys
from datetime import datetime

PY3 = sys.version_info > (3,)
if PY3:
    # noinspection PyUnresolvedReferences,PyCompatibility
    from urllib.parse import quote  # pragma: no cover
else:
    # noinspection PyUnresolvedReferences
    from urllib import quote

showall_url = 'twodo://x-callback-url/showAll'
showtoday_url = 'twodo://x-callback-url/showToday'
showstarred_url = 'twodo://x-callback-url/showStarred'
showscheduled_url = 'twodo://x-callback-url/showScheduled'


def get_add_url(task_title):
    """Return a url to add the task, represented by the arguments.
    :param task_title: The title of the task
    """
    return TwoDoTask.BASE_URL.format('task=' + quote(task_title))


# noinspection PyPep8Naming,PyAttributeOutsideInit
class TwoDoTask(object):
    """Represents all attributes of a task in the 2DoApp."""

    BASE_URL = 'twodo://x-callback-url/add?{}'
    TASK_TYPE = '0'
    PROJECT_TYPE = '1'
    CHECKLIST_TYPE = '2'

    PRIO_NONE = '0'
    PRIO_LOW = '1'
    PRIO_MEDIUM = '2'
    PRIO_HIGH = '3'

    DAILY = '1'
    WEEKLY = '2'
    BI_WEEKLY = '3'
    MONTHLY = '4'

    def __init__(self, task, task_type=TASK_TYPE, for_list=None,
                 for_parent_task=None, note=None, priority=PRIO_NONE,
                 starred=False, tags=None, due=None, dueTime=None, start=None,
                 repeat=None, action=None, ignoreDefaults=False, **_):
        """Create a TwoDoTask object."""
        self.task = task
        self.type = task_type
        self.for_list = for_list
        self.forParentTask = for_parent_task
        self.note = note
        self.priority = priority
        self.starred = starred
        self.tags = tags
        self.due = due
        self.dueTime = dueTime
        self.start = start
        self.repeat = repeat
        self.action = action
        self.ignoreDefaults = ignoreDefaults

    def url(self):
        """Return the URL for the task of this object."""
        urlpath = 'task=' + quote(self.task)
        if self.type != self.TASK_TYPE:
            urlpath += '&type={}'.format(self.type)
        if self.for_list is not None:
            urlpath += '&forlist={}'.format(quote(self.for_list))
        if self.note is not None:
            urlpath += '&note={}'.format(quote(self.note))
        if self.priority != self.PRIO_NONE:
            urlpath += '&priority={}'.format(self.priority)
        if self.starred == '1':
            urlpath += '&starred=1'
        if self.tags is not None:
            urlpath += '&tags={}'.format(quote(self.tags))
        if self.due is not None:
            urlpath += '&due={}'.format(quote(self.due))
        if self.dueTime is not None:
            urlpath += '&dueTime={}'.format(quote(self.dueTime))
        if self.start is not None:
            urlpath += '&start={}'.format(quote(self.start))
        if self.repeat is not None:
            urlpath += '&repeat={}'.format(self.repeat)
        if self.action is not None:
            urlpath += '&action={}'.format(quote(self.action))
        return self.BASE_URL.format(urlpath)

    @property
    def task(self):
        """The task's title text."""
        return self._task

    @task.setter
    def task(self, task_title):
        if task_title is None or len(task_title) == 0:
            raise ValueError('Task title must have content!')
        self._task = task_title

    @property
    def type(self):
        """Type of the task.

        One of TwoDoTask.TASK_TYPE, TwoDoTask.PROJECT_TYPE or
        TwoDoTask.CHECKLIST_TYPE.
        """
        return self._type

    @type.setter
    def type(self, task_type):
        task_type = str(task_type)
        if task_type not in [self.TASK_TYPE, self.PROJECT_TYPE,
                             self.CHECKLIST_TYPE]:
            msg = "Task type must be one of "
            msg += "'{}', '{}' or '{}', not '{}'".format(self.TASK_TYPE,
                                                         self.PROJECT_TYPE,
                                                         self.CHECKLIST_TYPE,
                                                         task_type)
            raise ValueError(msg)
        self._type = task_type

    @property
    def priority(self):
        """Priority of the task.

        One of TwoDoTask.PRIO_NONE, TwoDoTask.PRIO_LOW, TwoDoTask.PRIO_MEDIUM
        or TwoDoTask.PRIO_HIGH.
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        priority = str(priority)
        if priority not in [self.PRIO_NONE, self.PRIO_LOW, self.PRIO_MEDIUM,
                            self.PRIO_HIGH]:
            msg = "Task priority must be one of '{}', '{}', '{}' or '{}'"
            msg += ", not '{}'".format(self.PRIO_NONE,
                                       self.PRIO_LOW,
                                       self.PRIO_MEDIUM,
                                       self.PRIO_HIGH,
                                       priority)
            raise ValueError(msg)
        self._priority = priority

    @property
    def starred(self):
        """'1' if starred, otherwise '0'."""
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Determine the value for self._starred.

        for starred in [True, '1', 1]
        """
        self._starred = '1' if starred in [True, '1', 1] else '0'

    @property
    def ignoreDefaults(self):
        """If '1', ignore date and time defaults when storing task."""
        return self._ignoreDefaults

    @ignoreDefaults.setter
    def ignoreDefaults(self, ignoreDefaults):
        self._ignoreDefaults = '1' if ignoreDefaults in [True, '1', 1] else '0'

    @property
    def due(self):
        """The due date represented as: YYYY-mm-dd or as number of days."""
        return self._due

    @due.setter
    def due(self, due):
        # raise ValueError if wrong format (no int, no date)
        self._due = None
        if due is not None:
            try:
                int(due)
            except ValueError:
                datetime.strptime(due, '%Y-%m-%d')  # check format
            self._due = str(due)

    @property
    def dueTime(self):
        """The due date represented as: YYYY-mm-dd or as number of days."""
        return self._duetime

    @dueTime.setter
    def dueTime(self, duetime):
        # raise ValueError if wrong format (no int, no date)
        self._duetime = None
        if duetime is not None:
            datetime.strptime(duetime, '%H:%M')  # check format
            self._duetime = str(duetime)

    @property
    def start(self):
        """The start date and time.

        The formats are either  YYYY-mm-dd HH:MM or an int (number of days
        from today.
        """
        return self._start

    @start.setter
    def start(self, start):
        # raise ValueError if wrong format (no int, no date)
        self._start = None
        if start is not None:
            try:
                int(start)
            except ValueError:
                datetime.strptime(start, '%Y-%m-%d %H:%M')  # check format
            self._start = str(start)

    @property
    def repeat(self):
        """Repetition intervall of the task.

        One of TwoDoTask.DAILY, TwoDoTask.WEEKLY, TwoDoTask.BI_WEEKLY,
        TwoDoTask.MONTHLY.
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        if repeat not in [None, self.DAILY, self.WEEKLY, self.BI_WEEKLY,
                          self.MONTHLY]:
            msg = "Task repetition (repeat) must be one of "
            msg += "'{}', '{}', '{}' or '{}', not '{}'"
            msg = msg.format(self.DAILY, self.WEEKLY, self.BI_WEEKLY,
                             self.MONTHLY, repeat)
            raise ValueError(msg)
        self._repeat = repeat
