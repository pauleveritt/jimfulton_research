"""

Run this as python -m jimfulton_research.dump

"""

from .bootstrap import setup

with setup() as app:
    content = app.content
    f001 = content['f001']
    entries = f001.list_documents()
    print('\n'.join(entries))
