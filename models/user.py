from peewee import CharField, AutoField, DateField
from .database import BaseModel

class User(BaseModel):
    id = AutoField()
    name = CharField(max_length=50)
    birthday = DateField()

    class Meta:
        table_name = 'users'
