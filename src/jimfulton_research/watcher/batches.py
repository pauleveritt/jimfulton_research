import logging
from dataclasses import dataclass

from jimfulton_research.resources import Folder
from jimfulton_research.directory_watcher.models import Changeset
from jimfulton_research.directory_watcher.watchgod_watcher import FileChangeInfo
from zope.event import notify

logging.basicConfig(level=logging.INFO)


@dataclass
class NewBatch:
    changeset: Changeset


def handler_watcher(changeset: Changeset):
    """ Take directory_watcher info and broadcast zope.event """

    # This is the notify side of the zope.event subscription
    event = NewBatch(changeset=changeset)
    notify(event)


def handle_newbatch(content: Folder, event: NewBatch):
    """ Receive a ChangeSet event and update ZODB """

    # This is the subscribe side of the zope.event
    changes = event.changeset.changes

    # Walk through all the changes in this batch
    for change in changes:
        change_type = change.change_type
        file_path = change.file_path

        # For now, only handle change events
        if change_type is FileChangeInfo.modified:
            # Get the info needed from the changeset to
            # find the folder then the document in that folder
            parent = str(file_path.parent.name)
            name = str(file_path.name)
            doc = content[parent][name]

            # Replace the document's title attribute with the
            # contents of the file.
            with file_path.open() as f:
                title = f.read()
                doc.title = title
