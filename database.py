from peewee import OperationalError
from models import db, User, Category, Product, Order
from mock_data import random_order, random_user, random_product

import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def use_peewee():
    try:
        db.connect()
        db.create_tables([User, Category, Product, Order])
        print('Tables created successfully!')
        # random_product()
        # random_order()
        # get_products_by_quantity()
        # get_products_by_category()
    except OperationalError as e:
        print(f'Failed to connect to DB: {e}')
    finally:
        if not db.is_closed():
            db.close()
            print('Database connection closed.')


def get_products_by_quantity() -> None:
    query = Product.select().where(Product.quantity == 15)

    [print(f'{product.id}: {product.name} {product.price}') for product in query]

def get_products_by_category() -> None:
    query = (Product
             .select(Product, Category)
             .join(Category)
             .where(Product.category_id == 3))

    [print(f'{product.id}: {product.name} {product.price}') for product in query]

if __name__ == '__main__':
    use_peewee()
