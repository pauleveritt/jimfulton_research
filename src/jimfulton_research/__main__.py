from jimfulton_research.app import setup

with setup() as app:
    accounts = app['accounts']
    entries = accounts.list_accounts()
    print('\n'.join(entries))
