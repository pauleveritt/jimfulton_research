"""

Top-level container for research app

"""
from contextlib import contextmanager
from dataclasses import dataclass
from functools import partial
from inspect import getfile
from pathlib import Path

import transaction
from jimfulton_research.batches import handle_newbatch
from jimfulton_research.watcher.threadrunner import ThreadRunner
from zope.event import subscribers

from .batches import handler
from .resources import Folder


@dataclass
class App:
    content: Folder
    watcher: ThreadRunner


@contextmanager
def setup():
    from jimfulton_research.db import get_db
    from .resources import setup as content_setup

    db = get_db()
    with db.transaction() as connection:
        root = connection.root

        try:
            content = root.content
        except AttributeError:
            content = Folder()
            root.content = content
            content_setup(content)
            transaction.commit()

        # Setup the threadwatcher to get batches of changes
        content_root = Path(getfile(get_db)).parent / 'contents'
        assert content_root.exists()
        interval = 1
        watcher = ThreadRunner(
            handler,
            content_root,
            enabled=True,
            interval=interval,
        )

        # Wire up zope.event subscriber for new batches, notification
        # comes from the thread
        subscribers.append(
            partial(handle_newbatch, content, ),
        )

        app = App(content=content, watcher=watcher)
        yield app

    db.close()
