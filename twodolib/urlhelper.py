"""
Module to generate URLs to manage tasks, checlists and projects in 2DoApp.

see http://www.2doapp.com

"""

import urllib

showall_url = 'twodo://x-callback-url/showAll'
showtoday_url = 'twodo://x-callback-url/showToday'
showstarred_url = 'twodo://x-callback-url/showStarred'
showscheduled_url = 'twodo://x-callback-url/showScheduled'


_base_url = 'twodo://x-callback-url/add?{}'


def get_add_url(task_title):
    """Return a url to add the task, represented by the arguments."""
    return _base_url.format('task=' + urllib.quote(task_title))


class TwoDoTask(object):

    """Represents all attributes of a task in the 2DoApp."""

    TASK_TYPE = '0'
    PROJECT_TYPE = '1'
    CHECKLIST_TYPE = '2'

    def __init__(self, task_title, type=TASK_TYPE, for_list=None,
                 for_parent_task=None, note=None, priority=0, starred=0,
                 tags=None, due=None, due_time=None, start=None, repeat=None,
                 action=None, ignore_defaults=0):
        """Create a 2Do task.

        :type task_title: basestring
        """
        self.task = task_title
        self.type = type
        self.for_list = for_list
        self.forParentTask = for_parent_task
        self.note = note
        self.priority = priority
        self.starred = starred
        self.tags = tags
        self.due = due
        self.dueTime = due_time
        self.start = start
        self.repeat = repeat
        self.action = action
        self.ignoreDefaults = ignore_defaults
