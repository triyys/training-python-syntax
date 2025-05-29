from peewee import AutoField, IntegerField, ForeignKeyField
from .database import BaseModel
from .user import User
from .product import Product

class Order(BaseModel):
    id = AutoField()
    user_id = ForeignKeyField(User, backref='orders')
    product_id = ForeignKeyField(Product, backref='orders')
    quantity = IntegerField(default=0)

    class Meta:
        table_name = 'orders'
