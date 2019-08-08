import logging

from jimfulton_research.app import setup

logging.basicConfig(level=logging.INFO)

with setup() as app:
    try:
        logging.info('Starting watcher')
        app.watcher.start()
    except:
        logging.info('Stopping watcher...')
        app.watcher.stop()
        logging.info('Watcher stopped')
