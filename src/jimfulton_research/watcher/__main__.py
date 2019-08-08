from jimfulton_research.app import setup

with setup() as app:
    try:
        app.watcher.start()
    except:
        app.watcher.stop()
