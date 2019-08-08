# # account.py
#
# import persistent
# from persistent.mapping import PersistentMapping
# from dataclasses import dataclass
#
# from jimfulton_research.app import App
#
#
# class Accounts(PersistentMapping):
#     def list_accounts(self):
#         return [
#             f'Account {account.name}: {account.title}'
#             for account in self.values()
#         ]
#
#
# @dataclass(unsafe_hash=True)
# class Account(persistent.Persistent):
#     name: str
#     title: str
#
#
# def setup(app: App):
#     accounts = Accounts()
#     app['accounts'] = accounts
#
#     samples = {
#         Account(name='one', title='One'),
#         Account(name='two', title='Two'),
#         Account(name='three', title='Three'),
#         Account(name='four', title='Four'),
#     }
#     for sample in samples:
#         accounts[sample.name] = sample
