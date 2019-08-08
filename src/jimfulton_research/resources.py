from dataclasses import dataclass

from persistent import Persistent
from persistent.mapping import PersistentMapping


class Folder(PersistentMapping):
    def list_documents(self):
        return [
            f'Document {document.name}: {document.title}'
            for document in self.values()
        ]


@dataclass(unsafe_hash=True)
class Document(Persistent):
    name: str
    title: str


def setup(contents: Folder):
    samples = {
        Document(name='one', title='One'),
        Document(name='two', title='Two'),
        Document(name='three', title='Three'),
        Document(name='four', title='Four'),
    }
    for sample in samples:
        contents[sample.name] = sample
