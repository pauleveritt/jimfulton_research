"""

Top-level container for research app

"""
from contextlib import contextmanager

from BTrees.OOBTree import BTree


class App(BTree):
    pass
    # accounts: Accounts


@contextmanager
def setup():
    from .account import setup
    from jimfulton_research.db import get_db

    db = get_db()
    connection = db.open()
    root = connection.root

    try:
        app: App = root.app
    except AttributeError:
        app = App()
        root.app = app
        setup(app)

    yield app
    db.close()
