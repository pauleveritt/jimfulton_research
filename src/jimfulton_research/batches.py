import logging
from dataclasses import dataclass

from jimfulton_research.resources import Folder
from jimfulton_research.watcher.models import Changeset
from jimfulton_research.watcher.watchgod_watcher import FileChangeInfo
from zope.event import notify

logging.basicConfig(level=logging.INFO)


@dataclass
class NewBatch:
    changeset: Changeset


def handler(changeset: Changeset):
    event = NewBatch(changeset=changeset)
    notify(event)


def handle_newbatch(content: Folder, event: NewBatch):
    changes = event.changeset.changes
    for change in changes:
        change_type = change.change_type
        file_path = change.file_path
        if change_type is FileChangeInfo.modified:
            parent = str(file_path.parent.name)
            name = str(file_path.name)
            with file_path.open() as f:
                body = f.read()
                logging.info(body)
