from inspect import getfile
from pathlib import Path

from ZODB import DB, FileStorage


def get_db() -> DB:
    from jimfulton_research import bootstrap
    p = Path(getfile(bootstrap)).parents[2] / 'var' / 'Main.fs'
    fn = str(p)
    storage = FileStorage.FileStorage(fn)
    db = DB(storage)
    return db
