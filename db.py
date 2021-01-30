from peewee import SqliteDatabase
from peewee import Model
from peewee import DecimalField, DateField, CharField

db = SqliteDatabase("expense.db")


class BaseModel(Model):
    class Meta:
        database = db


class Expense(BaseModel):
    amount = DecimalField()
    purchase_date = DateField()
    merchant = CharField()


def init_database():
    db.init("expense.db")
    Expense.create_table()
