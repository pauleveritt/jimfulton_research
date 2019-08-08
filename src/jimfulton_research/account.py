# account.py

import persistent
from persistent.mapping import PersistentMapping
from pydantic.dataclasses import dataclass

from jimfulton_research.app import App


class Accounts(PersistentMapping):
    pass


@dataclass
class Account(persistent.Persistent):
    name: str
    title: str


def setup(app: App):
    app.accounts = accounts = Accounts()

    samples = {
        Account(name='one', title='One'),
        Account(name='two', title='Two'),
        Account(name='three', title='Three'),
        Account(name='four', title='Four'),
    }
    for sample in samples:
        accounts[sample.name] = sample
