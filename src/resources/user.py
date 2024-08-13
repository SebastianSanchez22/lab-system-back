from src.resources.session import Database
from src.entities.models.user import TblUsers


class UserResource():

    def __init__(self, credentials: dict):
        self.db = Database(credentials)
        self.table = TblUsers

    def get_all(self):
        results = self.db.get_all(self.table)
        return list(map(lambda result: result.as_dict(), results))
    
    def add_one(self, user: dict):
        self.db.add_one(item=self.table(**user))

    def update_one(self, id: int, user: dict):
        self.db.update_one(table=self.table, id=id, item=user)

    def disable_one(self, id: int):
        self.db.disable_one(table=self.table, id=id)

    def delete_one(self, id: int):
        self.db.delete_one(table=self.table, id=id)