"""

Console script to go into "server" mode, watch for changes, dispatch
ChangeSet events the main thread.

Run this as python -m jimfulton_research.watcher

"""

import logging

from jimfulton_research.bootstrap import setup

logging.basicConfig(level=logging.INFO)

with setup() as app:
    try:
        logging.info('Starting watcher')
        app.watcher.start()
    except:
        logging.info('Stopping watcher...')
        app.watcher.stop()
        app.db.close()
        logging.info('Watcher stopped')
