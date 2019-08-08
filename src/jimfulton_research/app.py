"""

Top-level container for research app

"""
import logging
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import transaction
from jimfulton_research.watcher.threadrunner import ThreadRunner

from .resources import Folder

logging.basicConfig(level=logging.INFO)


@dataclass
class App:
    content: Folder
    watcher: ThreadRunner


def handler(*args):
    logging.info('Handler called')


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
        content_root = Path('/tmp')
        enabled = True
        interval = 3
        watcher = ThreadRunner(
            handler, content_root, enabled=enabled, interval=interval,
        )

        app = App(content=content, watcher=watcher)
        yield app

    db.close()
