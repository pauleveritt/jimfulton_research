from .app import setup

with setup() as app:
    content = app.content
    entries = content.list_documents()
    print('\n'.join(entries))
