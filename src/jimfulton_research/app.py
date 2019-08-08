"""

Top-level container for research app

"""
from typing import Optional

import transaction
from BTrees.OOBTree import BTree
from ZODB import DB


class App(BTree):
    pass
    # accounts: Accounts


def setup(db: DB) -> Optional[App]:
    # noinspection PyUnusedLocal
    with db.transaction() as connection:
        connection = db.open()
        root = connection.root
        try:
            app = root.app
        except AttributeError:
            root.app = app = App()
            transaction.commit()

        return app
