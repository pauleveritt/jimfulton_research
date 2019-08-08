from ZODB import DB, FileStorage
import transaction

from jimfulton_research.account import Account, Accounts
from jimfulton_research.app import App


def get_app(root) -> App:
    try:
        app = root.app
    except AttributeError:
        root.app = app = App()
        app.accounts = accounts = Accounts()
        accounts['account-1'] = Account()
        transaction.commit()

    return app


def get_root():
    fn = '../../var/Main.fs'
    storage = FileStorage.FileStorage(fn)
    db = DB(storage)
    connection = db.open()
    root = connection.root

    return root


def main():
    root = get_root()
    app = get_app(root)
    print(app)


if __name__ == '__main__':
    main()
