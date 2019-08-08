"""

Dataclasses as models (or vice versa)

We have a number of dataclasses used as type hints. Let's move
here to avoid circular references.

"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Set

from .watchgod_watcher import FileChangeInfo


@dataclass(eq=True, frozen=True)
class ChangesetEntry:
    """ One changed file entry in a changeset """

    change_type: FileChangeInfo
    file_path: Path


@dataclass(frozen=True)
class Changeset:
    """ A collection of filesystem changes during an interval """

    timestamp: int
    changes: Set[ChangesetEntry] = field(default_factory=set)
