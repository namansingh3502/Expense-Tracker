class UserGroup:

    def set_members(self, members):

        self.members = members

    def add_expense(self, expense):
        self.expenses.append(expense)

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        self.expenses = []
