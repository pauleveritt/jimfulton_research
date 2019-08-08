"""

Top-level container for research app

"""
from contextlib import contextmanager
import logging
from pathlib import Path

import transaction
from BTrees.OOBTree import BTree
from jimfulton_research.watcher.threadrunner import ThreadRunner

logging.basicConfig(level=logging.INFO)


class App(BTree):
    pass


def handler(*args):
    logging.info('Handler called')


@contextmanager
def setup():
    from .account import setup
    from jimfulton_research.db import get_db

    db = get_db()
    with db.transaction() as connection:
        root = connection.root

        try:
            app: App = root.app
        except AttributeError:
            app = App()
            root.app = app
            setup(app)
            transaction.commit()

        # Setup the threadwatcher to get batches of changes
        content_root = Path('/tmp')
        enabled = True
        interval = 3
        watcher = ThreadRunner(
            handler, content_root, enabled=enabled, interval=interval,
        )
        try:
            watcher.start()
        except KeyboardInterrupt:
            watcher.stop()

        yield app

    db.close()
