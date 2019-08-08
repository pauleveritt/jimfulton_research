"""

Custom events for this addon.

"""
from dataclasses import dataclass

from .models import Changeset


@dataclass
class ChangesetEvent:
    """ Custom event with changeset and request """

    changeset: Changeset
