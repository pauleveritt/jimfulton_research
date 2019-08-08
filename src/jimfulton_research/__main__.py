from jimfulton_research.app import setup

app = setup()

with setup() as app:
    entries = app.accounts.list_accounts()
    print('\n'.join(entries))
