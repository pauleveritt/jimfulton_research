"""

Wrap the watcher in a thread to run it in the background.

"""
from pathlib import Path
from threading import Thread, Lock
from time import sleep
from typing import Callable, Optional

from .models import Changeset, ChangesetEntry
from .utils import epoch_seconds
from .watchgod_watcher import DefaultDirWatcher

log = __import__('logging').getLogger(__name__)


class ThreadRunner(Thread):
    """ Run a watcher in a thread """
    def __init__(self,
                 callback: Callable,
                 watched_path: Path,
                 enabled: bool,
                 interval: Optional[int],
                 ):
        super().__init__()
        self.callback = callback
        self.watched_path = watched_path
        self.enabled = enabled
        self.interval = interval
        self.lock = Lock()
        self.watcher = DefaultDirWatcher(str(watched_path))

    def run(self):
        while self.enabled:
            self.process_filesystem()

    def process_filesystem(self):
        """ Get changes from watcher, make changeset, hand to callback

        This is done as separate method for functional testing, to
        simulate changing a filesystem without running a thread.
        """
        changes = self.watcher.check()
        if changes:
            changeset = Changeset(timestamp=epoch_seconds(), changes={
                ChangesetEntry(change_type=i[0], file_path=Path(i[1]))
                for i in changes
            })
            self.callback(changeset)
        sleep(self.interval)

    def stop(self):
        self.enabled = False
