"""Modules and functions to add tasks to the 2Do App.

Create a task from python::

    >>> from twodolib import TwoDoTask
    >>> my_task = TwoDoTask('Save the world.', priority=TwoDoTask.PRIO_HIGH)

    >>> my_task.url()
    u'twodo://x-callback-url/add?task=Save%20the%20world.&priority=3'

Create a task, save it to 2DoApp and retrieve the task id:

    >>> my_task = TwoDoTask('Save the world.', priority=TwoDoTask.PRIO_HIGH, for_list="inbox")

    >>> # save the task in 2DoApp
    >>> import subprocess
    >>> subprocess.call(['open', my_task.url()])
    0

    >>> # retrieve taskid
    >>> my_task.get_taskid()
   '181378c217dd4f029a6ec7a47e65550d'
"""

__version__ = '0.5.4'

from .urlhelper import showall_url  # noqa
from .urlhelper import showtoday_url  # noqa
from .urlhelper import showstarred_url  # noqa
from .urlhelper import showscheduled_url  # noqa

from .urlhelper import TwoDoTask  # noqa

from .urlhelper import pbcopy, pbpaste  # noqa
