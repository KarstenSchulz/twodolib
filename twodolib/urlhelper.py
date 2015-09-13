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
