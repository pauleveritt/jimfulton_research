"""

Top-level container for research app

"""
from contextlib import contextmanager

import transaction
from BTrees.OOBTree import BTree


class App(BTree):
    pass


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

        yield app

    db.close()
