from peewee import CharField, AutoField
from .database import BaseModel

class Category(BaseModel):
    id = AutoField()
    name = CharField(max_length=100)

    class Meta:
        table_name = 'categories'
