from jimfulton_research.app import setup
from jimfulton_research.db import get_db
db = get_db()
app = setup(db)

entries = app.accounts.list_accounts()
print('\n'.join(entries))
