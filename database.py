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
        products1 = get_products_by_quantity(15)
        [print(f'{product.id}: {product.name} {product.price}') for product in products1]
        products2 = get_products_by_category(3)
        [print(f'{product.id}: {product.name} {product.price}') for product in products2]
    except OperationalError as e:
        print(f'Failed to connect to DB: {e}')
    finally:
        if not db.is_closed():
            db.close()
            print('Database connection closed.')


def get_products_by_quantity(quantity: int) -> list[Product]:
    query = Product.select().where(Product.quantity == quantity)

    return [product for product in query]

def get_products_by_category(category_id: int) -> list[Product]:
    query = (Product
             .select(Product, Category)
             .join(Category)
             .where(Product.category_id == category_id))

    return [product for product in query]

if __name__ == '__main__':
    use_peewee()
