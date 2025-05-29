from models import Order, Product, User
from faker import Faker
import random

fake = Faker()

def random_order(n_orders=10):
    user_query = User.select()
    product_query = Product.select()

    user_ids = [user.id for user in user_query]
    product_ids = [product.id for product in product_query]

    for _ in range(n_orders):
        Order.create(
            user_id=random.choice(user_ids),
            product_id=random.choice(product_ids),
            quantity=random.randint(1, 10),
        )
