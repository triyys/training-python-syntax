from peewee import AutoField, CharField, DecimalField, IntegerField, ForeignKeyField
from .database import BaseModel
from .category import Category

class Product(BaseModel):
    id = AutoField()
    name = CharField(max_length=150)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = IntegerField(default=0)
    category_id = ForeignKeyField(Category, backref='products')

    class Meta:
        table_name = 'products'
