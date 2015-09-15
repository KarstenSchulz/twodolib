"""
Module to generate URLs to manage tasks, checlists and projects in 2DoApp.

see http://www.2doapp.com

"""
from __future__ import unicode_literals
import sys

PY3 = sys.version_info > (3,)
if PY3:
    # noinspection PyUnresolvedReferences
    from urllib.parse import quote  # pragma: no cover
else:
    from urllib import quote


showall_url = 'twodo://x-callback-url/showAll'
showtoday_url = 'twodo://x-callback-url/showToday'
showstarred_url = 'twodo://x-callback-url/showStarred'
showscheduled_url = 'twodo://x-callback-url/showScheduled'


def get_add_url(task_title):
    """Return a url to add the task, represented by the arguments."""
    return TwoDoTask.BASE_URL.format('task=' + quote(task_title))


class TwoDoTask(object):

    """Represents all attributes of a task in the 2DoApp."""

    BASE_URL = 'twodo://x-callback-url/add?{}'
    TASK_TYPE = '0'
    PROJECT_TYPE = '1'
    CHECKLIST_TYPE = '2'

    def __init__(self, task, type=TASK_TYPE, for_list=None,
                 for_parent_task=None, note=None, priority='0', starred=False,
                 tags=None, due=None, dueTime=None, start=None, repeat=None,
                 action=None, ignoreDefaults=False):
        """Create a 2DoApp-task."""
        if len(task) == 0:
            raise ValueError('Task title must have content!')
        self.task = task
        self.type = type
        self.for_list = for_list
        self.forParentTask = for_parent_task
        self.note = note
        self.priority = priority
        if starred:
            self.starred = '1'
        else:
            self.starred = '0'
        self.tags = tags
        self.due = due
        self.dueTime = dueTime
        self.start = start
        self.repeat = repeat
        self.action = action
        if ignoreDefaults:
            self.ignoreDefaults = '1'
        else:
            self.ignoreDefaults = '0'

    def url(self):
        """Return the URL for the task of this object."""
        urlpath = 'task=' + quote(self.task)
        if self.type != '0':
            urlpath += '&type={}'.format(self.type)
        if self.for_list is not None:
            urlpath += '&for_list={}'.format(quote(self.for_list))
        return self.BASE_URL.format(urlpath)
