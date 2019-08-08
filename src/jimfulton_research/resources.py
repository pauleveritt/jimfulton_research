from dataclasses import dataclass
from inspect import getfile
from pathlib import Path

from ZODB import DB
from jimfulton_research.db import get_db
from jimfulton_research.directory_watcher.threadrunner import ThreadRunner
from persistent import Persistent
from persistent.mapping import PersistentMapping


@dataclass
class Folder(PersistentMapping):
    name: str = ''

    def __post_init__(self):
        super().__init__()

    def list_documents(self):
        return [
            f'Document {document.name}: {document.title}'
            for document in self.values()
        ]


@dataclass(unsafe_hash=True)
class Document(Persistent):
    name: str
    title: str


@dataclass
class App:
    content: Folder
    watcher: ThreadRunner
    db: DB


def setup(contents: Folder):
    # Make a f001 folder manually for now
    f001 = Folder(name='f001')
    contents['f001'] = f001

    content_root = Path(getfile(get_db)).parent / 'contents'
    for file_path in content_root.glob('**/*.txt'):
        # parent = str(file_path.parent.name)
        name = str(file_path.name)
        with file_path.open() as f:
            title = f.read()
            d = Document(name=name, title=title)
            f001[d.name] = d
