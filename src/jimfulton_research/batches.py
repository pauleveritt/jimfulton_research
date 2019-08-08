import logging
from dataclasses import dataclass

from jimfulton_research.resources import Folder
from jimfulton_research.watcher.models import Changeset
from jimfulton_research.watcher.watchgod_watcher import FileChangeInfo
from zope.event import notify

logging.basicConfig(level=logging.INFO)


@dataclass
class NewBatch:
    parent: str
    name: str
    body: str


def handler(content: Folder, changeset: Changeset):
    for change in changeset.changes:
        change_type = change.change_type
        file_path = change.file_path
        if change_type is FileChangeInfo.modified:
            parent = str(file_path.parent.name)
            name = str(file_path.name)
            with file_path.open() as f:
                body = f.read()
                event = NewBatch(
                    parent=parent,
                    name=name,
                    body=body,
                )
                notify(event)


def handle_newbatch(event: NewBatch):
    m = f'New batch: {event.parent}, {event.name}, {event.body}'
    logging.info(m)
